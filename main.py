from flask import Flask, request, url_for, render_template
from setup import *
import sys


app = Flask(__name__)


@app.route('/authorization', methods=['POST', 'GET'])
def authorization():
    if request.method == 'GET':
        return render_template('index.html')


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        list_data = [[{'image_url': 'https://assets.raribleuserdata.com/prod/v1/image/t_image_big/aHR0cHM6Ly9pcGZzLmlvL2lwZnMvYmFmeWJlaWQ1MmppaXU2Z3ZybHh0YWtmN3h5MnJ2Ynh3eGkzNHNzdjd2c2h3MzVsM2hvaGRkdDY3bGUvaW1hZ2UucG5n',
                          'name': 'Doctor Strange',
                          'description': 'Ticket to Doctor Strange premier',
                          'get_url': '/get_ticket/438823827'},
                     {
                         'image_url': 'https://assets.raribleuserdata.com/prod/v1/image/t_image_big/aHR0cHM6Ly9pcGZzLmlvL2lwZnMvYmFmeWJlaWhwcjQzNHRoZWJobnlieXV0ejVqbzczZXE1NGR1amhod2N3MmNpdjNvYWpuNHZvcG52bnEvaW1hZ2UucG5n',
                         'name': 'Jocker',
                         'description': 'Ticket to Joker premier',
                          'get_url': '/get_ticket/44328431'},
                     {
                         'image_url': 'https://ipfs.io/ipfs/bafybeie6ysnrkapuxkt3cpec5bcl2vrt23nrhoi3l5vdnd76ctuxtkbfpm/image.png',
                         'name': 'Nutcracker',
                         'description': 'Ticket to Nutcracker',
                         'get_url': '/get_ticket/432487877'}],
                     [{
                         'image_url': 'https://ipfs.io/ipfs/bafybeifivzm67sdr6bvujcrx4xmofs4i3tjkoeugpg7uxazoi3k4zttl34/image.png',
                         'name': 'Swan Lake',
                         'description': 'Ticket to Swan Lake',
                         'get_url': '/get_ticket/382818827'},
                     {
                         'image_url': 'https://assets.raribleuserdata.com/prod/v1/image/t_image_big/aHR0cHM6Ly9pcGZzLmlvL2lwZnMvYmFmeWJlaWZ4amx1czdvcDdtcnNuMmkzenNsZ3ZraHVxbmZ2d2ozYXJheHhsZWhxeGY1bWMzdGF5NGEvaW1hZ2UucG5n',
                         'name': 'Imagine Dragons concert',
                         'description': 'Ticket to Imagine Dragons concert',
                         'get_url': '/get_ticket/4714917193997'}]
                     ]
        return render_template('main_page.html', list_data=list_data)


@app.route('/get_ticket/<int:id>', methods=['POST', 'GET'])
def get_ticket(id):
    return render_template('get_ticket.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)
