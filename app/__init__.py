from flask import Flask


def create_app():
    app = Flask(__name__)

    import app.chrome_extension.controllers as box
    app.register_blueprint(box.module)

    import app.edu.controllers as health
    app.register_blueprint(health.module)

    return app