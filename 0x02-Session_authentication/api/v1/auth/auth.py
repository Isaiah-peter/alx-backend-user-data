#!/usr/bin/env python3
"""
Authentication
"""
from flask import request
from typing import List, TypeVar
from os import path as p
from os import getenv


class Auth():
    """auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """requires auth"""
        if (path is None):
            return True

        if (excluded_paths is None):
            return True

        if path[-1] != "/":
            path += "/"

        for paths in excluded_paths:
            if paths.endswith("*"):
                if paths.startswith(paths[:-1]):
                    return False
            elif path == paths:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """authorization header"""
        if request is None:
            return None

        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """current user"""
        return request

    def session_cookie(self, request=None):
        if request is None:
            return None

        SESSION_COOKIE = getenv("SESSION_NAME", None)
        return request.cookies.get(SESSION_COOKIE, None)
