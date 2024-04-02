from functools import wraps

import jwt
from flask import abort, current_app, request
from Hispanist_flask.my_app.models import User


def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        - does the Authorization header exist
        - does the token exist
        - token is not valid
        :param args:
        :param kwargs:
        :return:
        """
        if "Authorization" in request.headers:
            token = request.headers.get("Authorization")
            if token:
                try:
                    data = jwt.decode(token, current_app)
                    user = User.query.filter(User.email == data["email"]).first()
                    if not User:
                        return {"message": "User not found"}, 401
                    # if not check_password_hash(w)
                except Exception as e:
                    return {"message": "Invalid tojen", "error": e}, 401
            else:
                return {"message": "Authentication token required"}
        else:
            return {"message": "Authorization required"}
