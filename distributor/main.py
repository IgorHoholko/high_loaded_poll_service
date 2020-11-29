# -*- coding: utf-8 -*-
from flask import Flask, escape, request, jsonify
#import psycopg2
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from sqlalchemy.orm import sessionmaker
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:Asdfghjkl-9151290@db/poll_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

app = Flask(__name__)

#SQLALCHEMY_DATABASE_URI = "postgresql://postgres:Asdfghjkl-9151290@db/poll_db"
#SQLALCHEMY_TRACK_MODIFICATIONS = True	
#conn = psycopg2.connect(conn_string)
app.config.from_object(Config)
app.config['BUNDLE_ERRORS'] = True
app.debug = True
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

Session = sessionmaker(bind = engine)
session = Session()
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
import models as m

current_user = m.users.query.get(1)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'<h1> Hello, {escape(name)}! !!<h1>'


@app.route('/users', defaults={'user_id': None})
@app.route('/users/<user_id>')
def users(user_id):
    mm = [m.users.query.get(user_id)] if user_id != None else m.users.query.all()
    dm = [i.to_dict(i) for i in mm]
    return jsonify(dm)

@app.route('/new_user', methods = ['GET', 'POST'])
def new_user():
  if request.method == 'GET':
    mm = m.users.query.all()
    dm = [i.to_dict(i) for i in mm]
    return jsonify(dm)
  if request.method == 'POST':
    req = request.get_json(force = True)
    u = m.users(id=req.get('id'),name=req.get('name'),nickname=req.get('nickname'),language_code=req.get('language_code'),is_bot=req.get('is_bot'))
    u.add()
    return str(u.id)

@app.route('/questions', defaults={'question_id': None})
@app.route('/questions/<question_id>')
def questions(question_id):
    mm = [m.questions.query.get(question_id)] if question_id != None else m.questions.query.all()
    dm = [i.to_dict(i) for i in mm]
    return jsonify(dm)

@app.route('/new_question', methods = ['GET', 'POST'])
def new_question():
  if request.method == 'GET':
    mm = m.questions.query.all()
    dm = [i.to_dict(i) for i in mm]
    return jsonify(dm)
  if request.method == 'POST':
    req = request.get_json(force = True)
    q = m.questions(id=req.get('id'),text=req.get('text'))
    q.add()
    return str(q.id)

@app.route('/answers', defaults={'answer_id': None})
@app.route('/answers/<answer_id>')
def answers(answer_id):
    mm = [m.answers.query.get(answer_id)] if answer_id != None else m.answers.query.all()
    dm = [i.to_dict(i) for i in mm]
    return jsonify(dm)

@app.route('/new_answer', methods = ['GET', 'POST'])
def new_answer():
  if request.method == 'GET':
    mm = m.answers.query.all()
    dm = [i.to_dict(i) for i in mm]
    return jsonify(dm)
  if request.method == 'POST':
    req = request.get_json(force = True)
    q = m.answers(id=req.get('id'),text=req.get('text'),question_id=req.get('question'))
    q.add()
    return str(q.id)

@app.route('/choose_answer', methods = ['GET', 'POST'])
def choose_answer():
  if request.method == 'GET':
    mm = m.answers.query.all()
    q_id = request.args.get('question_id')
    dm = [i.to_dict(i) for i in mm]
    q = m.questions.query.get(q_id)
    dm.append({'question':q.to_dict(q)})
    return jsonify(dm)
  if request.method == 'POST':
    req = request.get_json(force = True)
    q = m.user_answer(id=req.get('id'),user_id=current_user.id,answer_id=req.get('answer'))
    q.add()
    return str(q.id)