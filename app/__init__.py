# -*- coding: UTF-8 -*-
# author:liujiayu
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'csrd_key'
app.config['SQLALCHEMY_DATABASE_URI'] = "xxxxx" #mysql+pymysql://user:password@ip:port/db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.debug = True
db=SQLAlchemy(app)



from app.web import web as web_blueprint
app.register_blueprint(web_blueprint)


