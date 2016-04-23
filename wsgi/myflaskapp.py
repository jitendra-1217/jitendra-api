from flask import Flask
app = Flask(__name__)

import config
app.config.from_object(config)

from flask.ext.basicauth import BasicAuth
basic_auth = BasicAuth(app)

from controllers.hello_controller import hello_bp
app.register_blueprint(hello_bp, url_prefix='/hello')

if __name__ == "__main__":
    app.run()
