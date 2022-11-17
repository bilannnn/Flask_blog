from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '710d19f48502d56f61334e369fc54202'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db: SQLAlchemy = SQLAlchemy(app)

from flaskblog import routes
