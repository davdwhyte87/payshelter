from flask import Flask

app=Flask(__name__,instance_relative_config=True)
app.config.from_object('config.settings')
app.config.from_pyfile('settings.py',silent=True)

@app.route('/')
def hello_world():
    return 'Whats up nigga! Thats the shit'
#run app
if __name__=='__main__':
    app.run()