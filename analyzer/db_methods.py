from flask import request, jsonify
import models as m

import os


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



@app.route('/delete_user/<user_id>', methods = ['POST'])
def delete_user(user_id):
    if user_id == 'all':
        u = m.users.query.all()
        [i.delete() for i in u]
    else:
        u = m.users.query.get(user_id)
        u.delete
    return 'ok'