from flask import Blueprint, request, jsonify
from repositories.repository_factory import RepositoryFactory

# بنعرف فلاسك إن ده جزء مفصول اسمه auth
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    # 1. نستقبل البيانات من المتصفح
    data = request.json
    username = data.get('username')
    email = data.get('email')
    password = data.get('password') # المفروض نعمل Hash هنا بعدين
    role = data.get('role')

    # 2. نطلب الـ Repository من المصنع
    user_repo = RepositoryFactory.get_repository("user")

    # 3. نضيف اليوزر
    try:
        user_repo.add_user(username, email, password, role)
        return jsonify({"message": "User registered successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400