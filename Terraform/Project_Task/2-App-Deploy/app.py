#Its Python app to deploy on the EC2 machine via Terraform..!

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Anand! This is Python Flash app"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)