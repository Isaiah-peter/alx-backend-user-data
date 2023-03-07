#!/usr/bin/env python3
"""
Authentication
"""
from flask import request
from typing import List, TypeVar
from os import path as p


class Auth():
    """auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """requires auth"""
        if (path == None):
            return True

        if (len(excluded_paths) == 0 or excluded_paths == None):
            return True

        if path[-1] != '/':
            path += '/'

        for paths in excluded_paths:
            if paths.endswith('*'):
                if path.startswith(paths[:-1]):
                    return False
            elif path == paths:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current user"""
        return None
