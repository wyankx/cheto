from flask import render_template, request, Flask, abort, jsonify, session
from flask_sqlalchemy import SQLAlchemy

import random
import string
import time

from web3.auto import w3
from eth_account.messages import defunct_hash_message

from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, set_access_cookies

app = Flask(__name__, static_url_path='/static')
app.jinja_env.add_extension('jinja2.ext.do')

app.config['JWT_SECRET_KEY'] = ''.join(random.choice(string.ascii_lowercase) for i in range(22))
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.secret_key = 'DkADKLJDJDSLKJDIFIYGIFDBFHbAE&t87qwte78T*D&ST'
app.config['JWT_COOKIE_SECURE'] = True
app.config['JWT_COOKIE_CSRF_PROTECT'] = True
jwt = JWTManager(app)


@app.route('/')
def auth():
    return render_template("index.html")


@app.route('/login', methods=['POST'])
def login():
    public_address = request.json[0]
    signature = request.json[1]
    original_message = 'Добро пожаловать в NFTICKETS! Нажмите кнопку "подписать", чтобы продолжить.\n\nWelcome to ' \
                       'NFTICKETS! Press the submit button to continue. '
    message_hash = defunct_hash_message(text=original_message)

    # UNIQUE CODE !!!!!
    signer = w3.eth.account.recoverHash(message_hash, signature=signature)

    access_token = create_access_token(identity=public_address)

    resp = jsonify({'login': True})
    set_access_cookies(resp, access_token)
    session['auth_nftickets'] = signer
    session['public_address'] = public_address

    return resp, 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
