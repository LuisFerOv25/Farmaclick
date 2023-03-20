from flask import Flask,abort
from flask import render_template
from flask import request,session
from administrador import administrador
from cliente import cliente
from auth import autenticar
from datetime import date
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
from werkzeug.exceptions import HTTPException
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from carrito import carro
from flask import make_response
from flask import jsonify
from datetime import timedelta
from os import listdir
from babel import numbers, dates
from datetime import date, datetime, time
from flask_babel import Babel, gettext, refresh; refresh()

app = Flask(__name__)
app.secret_key = '97110c78ae51a45af397be6534caef90ebb9b1dcb3380af008f90b23a5d1616bf19bc29098105da20fe'
import os
import babel.dates



os.environ.setdefault('BABEL_DEFAULT_LOCALE', 'es')
babel = Babel(app)
    
def get_locale():
    return request.accept_languages.best_match(['en', 'es', 'de', 'fr'])

babel = Babel(app, locale_selector=get_locale)

sentry_sdk.init(
    dsn="https://47b422c23c014fec8d53ccc9dc0e3e61@o4504709798952960.ingest.sentry.io/4504709801443328",
    integrations=[
        FlaskIntegration(),
    ],
    traces_sample_rate=1.0
)



app.register_blueprint(administrador)
app.register_blueprint(cliente)
app.register_blueprint(autenticar)
app.register_blueprint(carro)

error_codes = [
    400, 401, 403, 404, 405, 406, 408, 409, 410, 411, 412, 413, 414, 415,
    416, 417, 418, 422, 428, 429, 431, 451, 500, 501, 502, 503, 504, 505
]
for code in error_codes:
    @app.errorhandler(code)
    def client_error(error):
        return render_template('error.html', error=error), error.code


if __name__ == '__main__':
    app.run(debug=True, port=5711)


