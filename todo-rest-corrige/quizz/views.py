from .app import app
from flask import render_template, jsonify, abort, request, make_response, url_for
from .models import *


@app.route('/quiz/api/v1.0/questionnaires/', methods = ["GET"])
def get_questionnaires():
    return jsonify([(q.to_json()) for q in Questionnaire.query.all()])


@app.route('/quiz/api/v1.0/questionnaire/<int:quiz_id>', methods = ['GET'])
def get_questionnaire(quiz_id):
    print(quiz_id)
    q = Questionnaire.query.get(quiz_id)
    return q.to_json()


@app.route('/quiz/api/v1.0/questions/', methods = ["GET"])
def get_questions():
    return jsonify([(q.to_json()) for q in Question.query.all()])


@app.route('/quiz/api/v1.0/question/<int:quest_id>', methods = ['GET'])
def get_question(quest_id):
    q = Question.query.get(quest_id)
    return q.to_json()

@app.route('/quiz/api/v1.0/question/<int:quest_id>', methods = ['DELETE'])
def delete_question(quest_id):
    q = Question.query.get(quest_id)
    if q is None:
        abort(404)
    db.session.delete(q)
    db.session.commit()
    return jsonify( { 'result': True } )


@app.route('/quiz/api/v1.0/question/', methods = ['POST'])
def create_question():
    if not request.json or not 'title' in request.json or not 'type' in request.json or not 'idQuestionnaire' in request.json:
        abort(400)
    type_question = request.json['type']
    title_question = request.json['title']
    id_questionnaire = request.json['idQuestionnaire']
    print(type_question)
    match(type_question):
        case("SimpleQuestion"):
            firstAlternative = request.json['firstAlternative']
            secondAlternative = request.json['secondAlternative']
            q = SimpleQuestion(title = title_question, questionnaire_id = id_questionnaire, firstAlternative = firstAlternative, secondAlternative = secondAlternative)
        case("MultipleQuestion"):
            firstAlternative = request.json['firstAlternative']
            secondAlternative = request.json['secondAlternative']
            thirdAlternative = request.json['thirdAlternative']
            fourthAlternative = request.json['fourthAlternative']
            q = MultipleQuestion(title = title_question, questionnaire_id = id_questionnaire, firstAlternative = firstAlternative, secondAlternative = secondAlternative,
                third_Alternative = thirdAlternative, fourth_Alternative = fourthAlternative)
    db.session.add(q)
    db.session.commit()
    return jsonify( { 'questionnaire': q.to_json() } ), 201

@app.route('/quiz/api/v1.0/question/<int:quest_id>', methods = ['PUT'])
def update_question(quest_id):
    q = Question.query.get(quest_id)
    if q is None:
        abort(404)
    if not request.json:
        abort(400)
    
    q.title = request.json.get('title', q.title)
    q.question_type = request.json.get('type', q.question_type)
    db.session.commit()
    return jsonify( { 'question': q.to_json() } ),201

#Questionnaire

@app.route('/quiz/api/v1.0/questionnaire/<int:questionnaire_id>', methods = ['DELETE'])
def delete_questionnaire(questionnaire_id):
    q = Questionnaire.query.get(questionnaire_id)
    if q is None:
        abort(404)
    db.session.delete(q)
    db.session.commit()
    return jsonify( { 'result': True } )



@app.route('/quiz/api/v1.0/questionnaire/', methods = ['POST'])
def create_questionnaire():

    if not request.json or not 'name' in request.json:
        abort(400)
    name_questionnaire = request.json['name']
    q = Questionnaire(name = name_questionnaire)
    db.session.add(q)
    db.session.commit()
    return jsonify( { 'questionnaire': q.to_json() } ), 201

@app.route('/quiz/api/v1.0/questionnaire/<int:questionnaire_id>', methods = ['PUT'])
def update_questionnaire(questionnaire_id):
    q = Questionnaire.query.get(questionnaire_id)
    if q is None:
        abort(404)
    if not request.json:
        abort(400)
    
    q.name = request.json.get('name', q.name)
    db.session.commit()
    return jsonify( { 'questionnaire': q.to_json() } ),201



@app.errorhandler(400)
def bad_request(error):
    print(error)
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
    print(error)
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

"""@app.route('/quizz/api/v1.0/question/<int:task_id>', methods = ['PUT'])
def update_task(quest_id):
    q = Question.query.get(quest_id)
    if q is None:
        abort(404)
    if not request.json:
        abort(400)
    
    q.title = request.json.get('title', q.title)
    q.question_type = request.json.get('type', q.question_type)
    q.title = request.json.get('title', q.title)
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify( { 'task': make_public_task(task[0]) } )"""

"""
def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id = task['id'], _external = True)
        else:
            new_task[field] = task[field]
    return new_task
    
@app.route('/quizz/api/v1.0/tasks', methods = ['GET'])
def get_tasks():
    return jsonify(tasks=[ make_public_task(t) for t in tasks ])

@app.route('/quizz/api/v1.0/tasks/<int:task_id>', methods = ['GET'])
def get_task(task_id):
    task = list(filter(lambda t: t['id'] == task_id, tasks))
    if len(task) == 0:
        abort(404)
    return jsonify( { 'task': make_public_task(task[0]) } )

@app.route('/quizz/api/v1.0/tasks', methods = ['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': request.json.get('done', False), 
    }
    tasks.append(task)
    return jsonify( { 'task': make_public_task(task) } ), 201

@app.route('/quizz/api/v1.0/tasks/<int:task_id>', methods = ['PUT'])
def update_task(task_id):
    task = list(filter(lambda t: t['id'] == task_id, tasks))
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'done' not in request.json or type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify( { 'task': make_public_task(task[0]) } )
    
@app.route('/quizz/api/v1.0/tasks/<int:task_id>', methods = ['DELETE'])
def delete_task(task_id):
    task = list(filter(lambda t: t['id'] == task_id, tasks))
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify( { 'result': True } )"""
    