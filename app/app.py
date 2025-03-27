from flask import Flask
from .routes.main_routes import main_bp
import os

def create_app():
    app = Flask(__name__)
    app.config["UPLOAD_FOLDER"] = os.path.join(app.root_path, "..", "data", "uploads")
    app.config["PROCESSED_FOLDER"] = os.path.join(app.root_path, "..", "data", "processed")

    app.register_blueprint(main_bp)

    return app