from flask import Blueprint,request,session
from blueprints.user.inputes import RegisterInput,LoginInput
from blueprints.user.models import User,Token
from blueprints.model_schema import UserSchema
from flask import jsonify
from random import randint
from extensions import mail
from flask_mail import Message
from login_required import login_required
user_blueprint=Blueprint('user',__name__,template_folder='templates')

#this endpoint accepts (name,email,address,phone,state,password)
@user_blueprint.route('/signup',methods=('GET','POST'))
def signup():
    if request.method == "POST":
        inputs = RegisterInput(request)
        if inputs.validate():
            data = request.json
            user = User()
            user.encrypt_password(data['password'])
            user.name = data['name']
            user.email = data['email']
            user.phone = data['phone']
            user.address=data['address']
            user.state=data['state']
            user.code=randint(0,90000)
            user.save()
            # send_mail()
            return jsonify(code=1, message="User created Successfully")
        else:
            return jsonify(code=0, errors=inputs.errors, message="An error occured")
    return jsonify(code=0, message="An error occured")

def send_mail():
    msg=Message("This is a flask mail man!",recipients=["kingstonwhyte87@gmail.com"])
    msg.body="THis is a flask mail"
    msg.sender=["payshelter@gmail.com"]
    mail.send(msg)

@user_blueprint.route('/confirm_user/<code>')
def confirm_user(code):
    user = User.query.filter_by(code=code).first()
    if user:
        user.confirmed = 1
        user.save()
        #send user info mail
        return jsonify(code=1, message="User confirmed")
    else:
        return jsonify(code=0, message="Wrong confirmation code")


@user_blueprint.route('/login',methods=('GET','POST'))
def login():
    print(request.cookies.get('user',0))
    if request.method=="POST" :
        form = LoginInput(request)
        if form.validate():
            data=request.json
            email = data['email']
            user=User.query.filter_by(email=email).first()
            if user:
                if user.authenticate(user.password, data['password']):
                    import os
                    tk = Token()
                    tk.api_token = os.urandom(100)
                    tk.set_dates()
                    tk.user_id = user.id
                    tk.save()
                    return jsonify(code=1,token=tk.api_token)
                else:
                    return jsonify(code=0,message="Password or email is wrong")
            else:
                return jsonify(code=0,message="This user does not exist")
        else:
            return jsonify(code=0,success=False, errors=form.errors)
    else:
        return jsonify(code=0,message="An error occured")


@user_blueprint.route('/changepass',methods=('GET','POST'))
@login_required
def changepass():
    if request.method == "POST":
