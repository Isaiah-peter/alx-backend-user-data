#!/usr/bin/env python3
"""Basic Auth"""

import binascii
from api.v1.auth.auth import Auth
from base64 import b64decode
from typing import TypeVar, List
from models.user import User


class BasicAuth(Auth):
    """Basic Auth"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """extract base64 authorization header"""
        if authorization_header is None:
            return None

        if type(authorization_header) != str:
            return None

        if authorization_header[0:6] != "Basic ":
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """decode_base64_authorization_header"""
        if base64_authorization_header is None:
            return None

        if type(base64_authorization_header) != str:
            return None

        try:
            data_decode = b64decode(base64_authorization_header)
        except binascii.Error as err:
            return None

        return data_decode.decode('utf-8')

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """extract"""
        if decoded_base64_authorization_header is None:
            return (None, None)

        if type(decoded_base64_authorization_header) != str:
            return (None, None)

        if len(decoded_base64_authorization_header.split(":")) < 2:
            return (None, None)

        email, password = decoded_base64_authorization_header.split(':')

        return (email, password)


    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """user_object_from_credentials"""

        if user_email is None and type(user_email) != str:
            return None

        if user_pwd is None and type(user_pwd) != str:
            return None

        try:
            exist_user: List[TypeVar('User')]
            exist_user = User.search({"email": user_email})
        except Exception:
            return None

        for user in exist_user:
            if user.is_valid_password(user_pwd):
                return user

        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """current user"""
        header: str = self.authorization_header(request)

        if header is None:
            return None

        auth_head64: str = self.extract_base64_authorization_header(header)

        if auth_head64 is None:
            return None

        decode_auth: str = self.decode_base64_authorization_header(auth_head64)

        if decode_auth is None:
            return decode_auth

        mail: str
        passwd: str
        mail, passwd = self.extract_user_credentials(decode_auth)

        if mail is None or passwd is None:
            return None

        user_curr = self.user_object_from_credentials(mail, passwd)

        return user_curr
