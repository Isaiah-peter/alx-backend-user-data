#!/usr/bin/env python3
"""session auth"""

from api.v1.views import app_views
from flask import request, jsonify, make_response
from models.user import User
from os import getenv


@app_views.route("/auth_session/login", methods=["POST"], strict_slashes=False)
def login():
    """login"""
    email = request.form.get("email")
    password = request.form.get("password")

    if email is None:
        return make_response(jsonify({"error": "email missing"}), 400)

    if password is None:
        return make_response(jsonify({"error": "password missing"}), 400)

    user = User.search({"email": email})
    if len(user) == 0:
        return make_response(jsonify({"error": "no user found for this email"}), 404)

    if user.is_valid_password():
        return jsonify({"error": "wrong password"}), 401
    else:
        from api.v1.app import auth
        session_id = auth.create_session(user.get(id))
        SESSION_NAME = getenv("SESSION_NAME")
        response = make_response(user.to_json())
        response.set_cookie(SESSION_NAME, session_id)
        return response
