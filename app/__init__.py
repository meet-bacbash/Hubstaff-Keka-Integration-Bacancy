from app.extensions.db import app, create_db

def create_app():
    create_db()

    upload_folder = 'static/uploads'
    app.config['UPLOAD_FOLDER'] = upload_folder

    # file import

    from app.model import User
    # from app.forms.auth import LoginForm, RegistrationForm
    # from app.token.auth_middleware import token_required, token_already_exist
    # from app.extensions import db
    # from app.routes import log_in, logout_fun, register_user, main, blog, contact_us, course, teacher, single, about_us, user_profile, not_found
    # from app.model import auth
    # from app.forms import auth
    # from app.token import auth_middleware
    from app.extensions import db
    from app import routes

    return app
