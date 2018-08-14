from flask import Blueprint
from blueprints.user.models import User
user_blueprint=Blueprint('user',__name__,template_folder='templates')

@user_blueprint.route('/userm')
def user():
    return "heyoo user blue print works"