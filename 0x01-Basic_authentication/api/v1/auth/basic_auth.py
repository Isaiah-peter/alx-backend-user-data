#!/usr/bin/env python3
"""Basic Auth"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic Auth"""

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """extract base64 authorization header"""
        if authorization_header is None:
            return None
        
        if type(authorization_header) != str:
            return None
        
        if authorization_header[0:6] != "Basic ":
            return None
        
        return authorization_header[6:]