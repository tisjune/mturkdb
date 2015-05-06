from flask import Flask 


app = Flask(__name__)
app.config.from_object('config')

from mturkdb.views import accounts, admin, home, operations
from mturkdb import models