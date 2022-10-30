from setup import *
import sys
from flask import Flask


app = Flask(__name__)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)

