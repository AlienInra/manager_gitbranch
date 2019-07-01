# -*- coding: UTF-8 -*-
# author:liujiayu

from datetime import datetime
from app import db


class Model_name(db.Model):
    __tablename__="model"
    id = db.Column(db.Integer,primary_key=True)
    model_name = db.Column(db.String(100))
    create_time = db.Column(db.DateTime, index=True, default=datetime.now)


class Model_status(db.Model):
    __tablename__="model_status"
    id = db.Column(db.Integer,primary_key=True)
    model_name = db.Column(db.String(100))
    base_name = db.Column(db.String(100))
    to_branch = db.Column(db.String(100))
    status = db.Column(db.String(100))
    create_time = db.Column(db.DateTime, index=True, default=datetime.now)


if __name__ == '__main__':
    db.drop_all()
    db.create_all()