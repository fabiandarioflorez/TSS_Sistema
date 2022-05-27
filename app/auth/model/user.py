# Para majenar la base de datos
from app import db

# Para manejar formularios
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, HiddenField, EmailField, SelectField
from wtforms.validators import InputRequired, EqualTo, Length

from sqlalchemy import Enum

# Para majenar la encriptacion de las bases de datos
from werkzeug.security import check_password_hash, generate_password_hash

from app.utilities.model.role import RolUser
from app.utilities.model.estado import Estado

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    dni = db.Column( db.String(15) )
    nombres = db.Column( db.String(120) )
    apellido = db.Column( db.String(120) )
    segundo_apellido = db.Column( db.String(120) )
    telefono = db.Columnn( db.String(15) )
    correo = db.Column(db.String(255) )
    username = db.Column(db.String(255) )
    password_hash = db.Column(db.String(300))
    role = db.Column(Enum(RolUser))
    estado = db.Column(Enum(Estado))

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __init__(self,
        dni:str,
        nombres:str,
        apellido:str,
        segundo_apellido:str,
        telefono:str,
        correo:str,
        username:None, 
        password_hash, 
        role = RolUser.regular,
        estado = Estado.activo):

        self.dni = dni
        self.nombres = nombres
        self.apellido = apellido
        self.segundo_apellido = segundo_apellido
        self.telefono = telefono
        self.correo = correo
        self.username = username
        self.password_hash = generate_password_hash(password_hash)
        self.role = role
        self.estado = estado

    def __repr__(self) -> str:
        return '<User %r>' % (self.username)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Formulario para el registro
class RegisterForm(FlaskForm):
    nombres = StringField('Nombres', validators=[InputRequired(),Length(max=255)])

    apellido = StringField('Apellido', validators=[InputRequired(),Length(max=255)])

    segundo_apellido = StringField('Segundo apellido', validators=[Length(max=255)])

    telefono = StringField('Telefono', validators=[InputRequired(), Length(min=10,max=15)])

    correo = EmailField('Correo',validators=[InputRequired(), Length(max=255)])

    username = StringField('Usuario', validators=[InputRequired()])

    password = PasswordField('Password', validators=[InputRequired(),EqualTo('confirm')])
    
    role = SelectField('Rol',choices=[ ('regular', 'regular'), ('admin', 'admin')])

    estado = SelectField('Rol',choices=[ ('activo', 'activo'), ('bloqueado', 'bloqueado')])

    confirm  = PasswordField('Repetir la contraseña')

# No lo utilizamos
class UserForm(FlaskForm):
    username = StringField('Usuario', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

# Formulario para el logeo
class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    next = HiddenField('next')


