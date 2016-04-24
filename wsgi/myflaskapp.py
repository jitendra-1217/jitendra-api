from flask import Flask
app = Flask(__name__)

import config
app.config.from_object(config)

from flask.ext.basicauth import BasicAuth
basic_auth = BasicAuth(app)

# Setup logging
import logging
import logging.handlers
formatter = logging.Formatter(
    "%(asctime)s - %(pathname)s:%(lineno)d\n%(levelname)s - %(message)s\n")
handler = logging.handlers.RotatingFileHandler(
    app.config['LOG_FILENAME'],
    maxBytes=10000000,
    backupCount=5)
handler.setLevel(app.config['LOG_LEVEL'])
handler.setFormatter(formatter)
app.logger.addHandler(handler)

from controllers.hello_controller import hello_bp
app.register_blueprint(hello_bp, url_prefix='/hello')

from controllers.daily_log_controller import daily_log_bp
app.register_blueprint(daily_log_bp, url_prefix='/dailylog')

if __name__ == "__main__":
    app.run()
