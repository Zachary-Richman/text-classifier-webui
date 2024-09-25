import os
from flask import flash, request, redirect, jsonify, Blueprint, render_template # type: ignore
from werkzeug.utils import secure_filename # type: ignore

from helpers.server.file_handling import allowed_file
from helpers.excel.excel_manip import ExcelManip

# ============================ #
UPLOAD_FOLDER: str = "./UserUploads"  # MODIFIABLE. THIS IS A PATH TECHNICALLY
# ============================ #

excel_helper: ExcelManip = ExcelManip(UPLOAD_FOLDER)

file_handling = Blueprint('File Handling', __name__, template_folder='templates')
# file_handling.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@file_handling.route('/upload-file', methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if 'file' not in request.files:
            flash('No File Part')
            return redirect(request.url)
        
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
    
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(f'.{UPLOAD_FOLDER}', filename))
    
    return render_template('upload-file.html')


@file_handling.route('/view-all-files', methods=["GET"])
def pull_all_files():
    # Pulls all files uploaded onto the UserUploads file
    all_files = excel_helper.pull_all_excel_files()
    print(all_files)
    return jsonify(all_files[0]['files'])


@file_handling.route('/view-all-files/<filename>', methods=["GET"])
def pull_all_sheetnames(filename: str):
    all_sheets = excel_helper.pull_sheet_names(filename=filename)
    return jsonify(all_sheets)
 