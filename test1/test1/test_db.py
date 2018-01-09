#encoding: utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'Fianna'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://xianjun666:lovedcn@localhost:'


