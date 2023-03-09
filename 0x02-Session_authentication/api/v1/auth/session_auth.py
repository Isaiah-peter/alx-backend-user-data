#!/usr/bin/env python3
"""session Auth"""

from api.v1.auth.auth import Auth
import uuid


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
