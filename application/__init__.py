from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kavehmollaei'
#Running and Controlling the script


from application import routes


if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True,port=1213)