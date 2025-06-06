#Test the app on the EC2 Instance
from flask import Flask

app = Flask(__name__)


@app.route("/")   #It initiate the app and provide addtional Error message
def hello():
    return "Hey Anand Saini..!"

app.run("0.0.0.0")