from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return "Hello, World!"
if__name__ == "__rain__":
    app.run(debug=True)
