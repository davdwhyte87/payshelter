from flask import Flask
from extensions import login_manager
from extensions import db,migrate,ma,cors

app=Flask(__name__,instance_relative_config=True)
app.config.from_object('config.settings')
app.config.from_pyfile('settings.py',silent=True)

from blueprints.user.user import user_blueprint

#test route
@app.route('/')
def hello_world():
    return 'Sup sup!'

#initialize app blue prints
app.register_blueprint(user_blueprint)


#initialize extensions
db.init_app(app)
login_manager.init_app(app)
ma.init_app(app)
cors.init_app(app)

#run app
if __name__=='__main__':
    app.run()