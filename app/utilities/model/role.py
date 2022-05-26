from flask import flash, redirect, url_for
from flask_login import current_user, logout_user


from functools import wraps

import enum


"""Clase RolUser

Para utilizar roles

"""


class RolUser(enum.Enum):
    regular='regular'
    admin='admin'

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