from flask import Flask
app = Flask(__name__)
from application import routes

#Running and Controlling the script
if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True,port=1213)