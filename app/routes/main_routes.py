from flask import Blueprint, render_template, request, current_app
from app.services.document_service import process_uploaded_pdf
import os

main_bp = Blueprint('main', __name__)

@main_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["pdf"]
        if file:
            # Caminho absoluto baseado na raiz do app
            upload_folder = os.path.abspath(os.path.join(current_app.root_path, "..", "data", "uploads"))
            os.makedirs(upload_folder, exist_ok=True)

            filepath = os.path.join(upload_folder, file.filename)
            file.save(filepath)

            processed_data = process_uploaded_pdf(filepath)
            return render_template("index.html", data=processed_data)

    return render_template("index.html", data=None)