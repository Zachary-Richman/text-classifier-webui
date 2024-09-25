# from helpers.server.routes.uploading_files import ALLOWED_EXTENSIONS  // creates circular import

ALLOWED_EXTENSIONS = {'xlsx', 'xls', 'xlbs'}  # MODIFIFABLE.


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

