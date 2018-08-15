from flask_wtf import FlaskForm
from flask_inputs import Inputs
from wtforms import StringField,IntegerField,PasswordField
from wtforms_components import EmailField
from wtforms.validators import DataRequired,Length

class RegisterInput(Inputs):
  json={
      'name':[DataRequired("name field is required")],
      'email':[DataRequired("Email field is required")],
      'phone':[DataRequired("phone field is required")],
      'password':[DataRequired("Password is required")],
      'state':[DataRequired("The user type is required")],
      'address':[DataRequired("The user type is required")]
  }
class ChangePassInputs(Inputs):
   json={
       'email': [DataRequired("Email field is required")],
       'current': [DataRequired("Password is required")]
   }

class LoginInput(Inputs):
   json={
       'email': [DataRequired("Email field is required")],
       'password': [DataRequired("Password is required")]
   }

class UpdateForm(Inputs):
    json = {
        'name': [DataRequired("name field is required")],
        'email': [DataRequired("Email field is required")],
        'phone': [DataRequired("phone field is required")]
    }