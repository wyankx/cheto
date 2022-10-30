from flask import Flask, request, url_for, render_template


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html', url='')


if __name__ == '__main__':
    app.run(port=8081, host='localhost')