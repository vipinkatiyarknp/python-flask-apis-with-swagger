from flask import Flask
# from api.elastic_test import connect_elasticsearch

# es = connect_elasticsearch()

app = Flask(__name__)

from apis.root import *
from apis.get_user import *
from apis.get_users import *


if __name__ == '__main__':
    app.run()