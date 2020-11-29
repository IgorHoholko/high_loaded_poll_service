from main import app, db, engine
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.orderinglist import ordering_list
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from datetime import date
from flask_login import UserMixin
from sqlalchemy import CheckConstraint, Sequence, func, inspect
from sqlalchemy.orm import load_only, MapperExtension, mapper
from sqlalchemy.ext.declarative import declared_attr, declarative_base

class users(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    nickname = db.Column(db.String(256), nullable=False, unique=True)
    language_code = db.Column(db.Text(), nullable=False)
    is_bot = db.Column(db.Boolean(), nullable=False)

    @staticmethod
    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    def add(self):
        db.session.add(self)
        db.session.commit()


class questions(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(256), nullable=False)

    @staticmethod
    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    def add(self):
        db.session.add(self)
        db.session.commit()

class answers(db.Model):
    __tablename__ = 'answers'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(256), nullable=False)
    question_id = db.Column(db.SmallInteger, db.ForeignKey('questions.id'), nullable=False)
    @staticmethod
    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

    def add(self):
        db.session.add(self)
        db.session.commit()

class user_answer(db.Model):
    __tablename__ = 'user_answer'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.SmallInteger, db.ForeignKey('users.id'), nullable=False)
    answer_id = db.Column(db.SmallInteger, db.ForeignKey('answers.id'), nullable=False)
    @staticmethod
    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
    

    def add(self):
        db.session.add(self)
        db.session.commit()

