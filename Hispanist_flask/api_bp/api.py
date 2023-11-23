from flask import Blueprint, jsonify, request, current_app, abort
from Hispanist_flask.my_app.models import User
import jwt
from datetime import datetime, timedelta, timezone


api_bp = Blueprint('api', __name__, template_folder='templates', static_folder='static', url_prefix='/api')


@api_bp.route('/')
def api_index():
    return jsonify({'status': 200})


@api_bp.route('/get_user', methods=['GET', 'POST'])
def get_user():
    if request.method == 'POST':
        user_id = request.json.get('id')
        user = User.query.filter(User.id==user_id).first()
        result = {
            user.id: {
                'name': user.name, 
                'username': user.username,
                'role': user.role
            }
        }
        return jsonify(result)


@api_bp.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        login = request.json.get('login')
        password = request.json.get('password')
        exp = datetime.now(tz=timezone.utc) + timedelta(hours=1)
        token = jwt.encode(dict(login=login, password=password, exp=exp), current_app.secret_key, algorithm='HS256')
        return {'status': 'token generated sucessfully', 'token': token}
    return abort(405)
