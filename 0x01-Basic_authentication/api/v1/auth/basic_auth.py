#!/usr/bin/env python3
"""Basic Auth"""

import binascii
from api.v1.auth.auth import Auth
from base64 import b64decode


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
        if base64_authorization_header == None:
            return None

        if type(base64_authorization_header) != str:
            return None

        try:
            data_decode = b64decode(base64_authorization_header)
        except binascii.Error as err:
            return None

        return data_decode.decode('utf-8')
