#!/usr/bin/env python3
"""session Auth"""

from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """session Auth"""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """create session"""
        if user_id is None:
            return None

        if type(user_id) != str:
            return None

        id = str(uuid.uuid4())

        self.user_id_by_session_id[id] = user_id
        return id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """user id for session"""
        if session_id is None:
            return None

        if type(session_id) != str:
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """current user"""
        cookie_value = self.session_cookie(request)
        id = self.user_id_for_session_id(cookie_value)
        return User.get(id)
