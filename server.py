from flask import Flask, render_template # type: ignore

# Helper Imports
from helpers.server.routes.uploading_files import file_handling as file_handling_route


app = Flask(__name__)
app.register_blueprint(file_handling_route)

@app.route('/select')
def select():
    return render_template('select.html')

app.run(host='0.0.0.0', port=8080, debug=True)