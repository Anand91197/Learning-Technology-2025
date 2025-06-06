#Test Flask app
#Need to install Flask on the EC2 Instnace

from flask import Flask
app = Flask(__name__) #Creating a flask app instance

@app.route("/")  #It handle additional Error message
def hello():
    return "Hey Anand Saini..!!"

app.run("0.0.0.0")