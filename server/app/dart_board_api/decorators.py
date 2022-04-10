from functools import wraps
from flask import request, jsonify, current_app
import jwt


def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'Alert': 'Token is missing'}), 403
        try:
            payload = jwt.decode(token, current_app.config['SECRET_KEY'])
        except:
            return jsonify({'Alert': 'Invalid Token'}), 403

        return func(*args, **kwargs)
    return decorated
