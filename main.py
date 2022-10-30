from flask import Flask, request, url_for, render_template, session, jsonify
from setup import *
import sys
import random
import string
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, set_access_cookies


app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.do')

app.config['JWT_SECRET_KEY'] = ''.join(random.choice(string.ascii_lowercase) for i in range(22))
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.secret_key = os.environ.get('SECRET_KEY')
app.config['JWT_COOKIE_SECURE'] = True
app.config['JWT_COOKIE_CSRF_PROTECT'] = True
jwt = JWTManager(app)


@app.route('/authorization', methods=['POST', 'GET'])
def authorization():
    if request.method == 'GET':
        return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        list_data = [[{'image_url': 'https://assets.raribleuserdata.com/prod/v1/image/t_image_big/aHR0cHM6Ly9pcGZzLmlvL2lwZnMvYmFmeWJlaWQ1MmppaXU2Z3ZybHh0YWtmN3h5MnJ2Ynh3eGkzNHNzdjd2c2h3MzVsM2hvaGRkdDY3bGUvaW1hZ2UucG5n',
                      'name': 'Doctor Strange',
                      'description': 'Ticket to Doctor Strange premier'},
                     {
                         'image_url': 'https://assets.raribleuserdata.com/prod/v1/image/t_image_big/aHR0cHM6Ly9pcGZzLmlvL2lwZnMvYmFmeWJlaWQ1MmppaXU2Z3ZybHh0YWtmN3h5MnJ2Ynh3eGkzNHNzdjd2c2h3MzVsM2hvaGRkdDY3bGUvaW1hZ2UucG5n',
                         'name': 'Doctor Strange',
                         'description': 'Ticket to Doctor Strange premier'},
                     {
                         'image_url': 'https://assets.raribleuserdata.com/prod/v1/image/t_image_big/aHR0cHM6Ly9pcGZzLmlvL2lwZnMvYmFmeWJlaWQ1MmppaXU2Z3ZybHh0YWtmN3h5MnJ2Ynh3eGkzNHNzdjd2c2h3MzVsM2hvaGRkdDY3bGUvaW1hZ2UucG5n',
                         'name': 'Doctor Strange',
                         'description': 'Ticket to Doctor Strange premier'}],
                     [{
                         'image_url': 'https://assets.raribleuserdata.com/prod/v1/image/t_image_big/aHR0cHM6Ly9pcGZzLmlvL2lwZnMvYmFmeWJlaWQ1MmppaXU2Z3ZybHh0YWtmN3h5MnJ2Ynh3eGkzNHNzdjd2c2h3MzVsM2hvaGRkdDY3bGUvaW1hZ2UucG5n',
                         'name': 'Doctor Strange',
                         'description': 'Ticket to Doctor Strange premier'},
                     {
                         'image_url': 'https://assets.raribleuserdata.com/prod/v1/image/t_image_big/aHR0cHM6Ly9pcGZzLmlvL2lwZnMvYmFmeWJlaWQ1MmppaXU2Z3ZybHh0YWtmN3h5MnJ2Ynh3eGkzNHNzdjd2c2h3MzVsM2hvaGRkdDY3bGUvaW1hZ2UucG5n',
                         'name': 'Doctor Strange',
                         'description': 'Ticket to Doctor Strange premier'}]
                     ]
        return render_template('main_page.html', list_data=list_data)


@app.route('/login', methods=['POST'])
def login():
    public_address = request.json[0]
    signature = request.json[1]
    original_message = 'Добро пожаловать в NFTICKETS! Нажмите кнопку "подписать", чтобы продолжить.\n\nWelcome to ' \
                       'NFTICKETS! Press the submit button to continue. '
    message_hash = defunct_hash_message(text=original_message)

    signer = w3.eth.account.recoverHash(message_hash, signature=signature)

    access_token = create_access_token(identity=public_address)

    resp = jsonify({'login': True})
    set_access_cookies(resp, access_token)
    session['auth_nftickets'] = signer
    session['public_address'] = public_address

    return resp, 200


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)
