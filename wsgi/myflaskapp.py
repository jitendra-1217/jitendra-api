from flask import Flask
app = Flask(__name__)

import config
app.config.from_object(config)

from flask.ext.basicauth import BasicAuth
basic_auth = BasicAuth(app)


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/secret")
@basic_auth.required
def secret():
    return "Secret message!"

if __name__ == "__main__":
    app.run()
