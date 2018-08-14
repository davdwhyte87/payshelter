from flask import Blueprint
from blueprints.user.models import User
from blueprints.model_schema import UserSchema
from flask import jsonify

user_blueprint=Blueprint('user',__name__,template_folder='templates')

@user_blueprint.route('/usertest')
def user():
    user = User()
    user.name = "david"
    user.email = "david@gmail.com"
    user.phone = "090798990"
    user.password = "kllkslkslslsl"
    user.save()
    return "heyoo user blue print works"

@user_blueprint.route('/getuser')
def user_get():
    users = User.query.all()
    post_schema = UserSchema(many=True)
    output = post_schema.dump(users).data
    return jsonify(users=output)
