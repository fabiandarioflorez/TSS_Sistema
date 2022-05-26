
from flask import Blueprint, Flask, redirect, url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user, logout_user
from flask_cors import CORS

from functools import wraps

app = Flask(__name__)

# Configuramos la conexion de base de datos
app.config.from_object('./config/config.DevelopmentConfig')

#CORS
cors = CORS(app, resources={
    r"/api/*": {
        "origins":"http://localhost:8080"
    }
})

db = SQLAlchemy(app)

# Para implementar login manager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'fauth.login'

# definimos nuestro decorador
def role_admin_need(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        if current_user.role.value != 'admin':
            logout_user()
            flash('No tiene permisos para ingresar','danger')
            return redirect(url_for('fauth.login'))
            # login_manager.unauthorized()
            # print('Holaaaa aaaa Calling decorated '+str(current_user.role.value) )
        return f(*args, **kwds)
    return wrapper

# from app.product.productControler import product
# from app.product.categoryControler import category
# # from app.auth.authControler import auth
# from app.fauth.fauthControler import fauth

# # rest
# from app.rest_api.product_api import product_view
# from app.rest_api.category_api import category_view

# # registramos Blueprint
# # app.register_blueprint(auth)
# app.register_blueprint(fauth)
# app.register_blueprint(product)
# app.register_blueprint(category)

# # Lo llamamos al final
# db.create_all()
