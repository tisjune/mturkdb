from flask import Flask 
from flask.ext.sqlalchemy import SQLAlchemy  
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)



from mturkdb.views import accounts, admin, attributes, home, operations
from mturkdb import models, utils