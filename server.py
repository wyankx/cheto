import requests
from flask import render_template, request, Flask, jsonify, session, redirect

import random
import string

from eth_account.messages import defunct_hash_message

from flask_jwt_extended import JWTManager, create_access_token, set_access_cookies

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
    print(session)
    if 'public_address' in session:
        return redirect('/events')
    try:
        nfts = get_nfts(session['public_address'])
    except:
        nfts = []
    return render_template("index.html", nfts=nfts)

@app.route('/events')
def events():
    if 'public_address' not in session:
        return redirect('/')
    d = get_nfts(session['public_address'])
    print(d)
    data = d
    data = [d[i:i+3] for i in range(len(d))]
    return render_template('events.html', list_data=data)

@app.route('/get_ticket/<int:id>', methods=['POST', 'GET'])
def get_ticket(id):
    return render_template('get_ticket.html')

@app.route('/login', methods=['POST'])
def login():
    public_address = request.json[0]
    signature = request.json[1]
    original_message = 'Добро пожаловать в NFTICKETS! Нажмите кнопку "подписать", чтобы продолжить.\n\nWelcome to ' \
                       'NFTICKETS! Press the submit button to continue. '
    message_hash = defunct_hash_message(text=original_message)

    access_token = create_access_token(identity=public_address)

    resp = jsonify({'login': True})
    set_access_cookies(resp, access_token)
    session['public_address'] = public_address
    print('aaa')
    return resp, 200


def get_nfts(address):
    d = requests.get(f'https://api.rarible.org/v0.1/items/byOwner?owner=ETHEREUM:{address}')
    return [x['meta'] for x in d.json()['items']]


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
