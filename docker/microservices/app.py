from flask import Flask, render_template, send_from_directory
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__, template_folder="templates")
CORS(app)

APP_PORT = os.getenv("APP_PORT")
CERTFILE = os.getenv("CERT_FILE")
KEYFILE = os.getenv("KEY_FILE")

SWAGGER_URL = '/api-doc'
API_URL = '/static/aaa.yaml'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config = {
        'app_name': "SKOR"
    }
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route("/")
def home():
    return send_from_directory("templates", "index.html")

@app.route('/<path:path>')
def send_path(path):
    return send_from_directory("templates", path)

if __name__=='__main__':
    if os.getenv("LOCAL") == 'False':
        app.run(ssl_context=(CERTFILE, KEYFILE), host='0.0.0.0', port=APP_PORT, debug=True)
    else:
        app.run(host='0.0.0.0', port=APP_PORT, debug=True)
    