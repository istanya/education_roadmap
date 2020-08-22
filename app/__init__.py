from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True

    import app.chrome_extension.controllers as extension
    app.register_blueprint(extension.module)

    import app.edu.controllers as edu
    app.register_blueprint(edu.module)

    return app