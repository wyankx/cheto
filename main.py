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


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)
