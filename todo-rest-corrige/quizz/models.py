from .app import db
from flask import url_for

class Questionnaire(db.Model):
    id   = db.Column(db.Integer, 
        primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Questionnaire (%d) %s>" % (self.id, self.name)

    def to_json(self):
        json_questionnaire = {
            'url': url_for('get_questionnaire', 
                quiz_id=self.id, _external=True),
            'name': self.name,
            'id': self.id,
            'questions': 
            [ q.to_json()['url'] for q in self.questions ]
        }
        return json_questionnaire

class Question(db.Model):
    id     = db.Column(db.Integer, 
        primary_key=True)
    title  = db.Column(db.String(120))
    question_type = db.Column(db.String(12))
    questionnaire_id = db.Column(db.Integer, 
        db.ForeignKey('questionnaire.id'))
    questionnaire = db.relationship("Questionnaire",
        backref=db.backref("questions", 
        lazy="dynamic",
        cascade="all, delete-orphan"))

    def __repr__(self):
        return "<Question (%d) %s>" % (self.id, self.title)

    def to_json(self):
        json_quest = {
            'url': url_for('get_question',
             quest_id=self.id, _external=True),
            'questionnaire_url': url_for('get_questionnaire'
                , quiz_id=self.questionnaire_id,
                 _external=True),
            'title': self.title,
            'question_type': self.question_type,
            'question':self.json_content()
            }
        return json_quest
    __mapper_args__ = {
        "polymorphic_identity":"Question",
        "with_polymorphic": "*",
        "polymorphic_on": "question_type"
    }

class SimpleQuestion(Question):
    firstAlternative = db.Column(db.String(120))
    secondAlternative = db.Column(db.String(120))
    firstChecked = db.Column(db.Boolean)

    def json_content(self):
        json_quest = dict()
        json_quest['firstAlternative'] = self.firstAlternative
        json_quest['secondAlternative'] = self.secondAlternative
        return json_quest
    __mapper_args__ = {
        'polymorphic_identity': 'SimpleQuestion',
        'with_polymorphic': '*',
        "polymorphic_load": "inline"
    }

class TexteQuestion(Question):

    def json_content(self):
        json_quest = dict()
        return json_quest
    __mapper_args__ = {
        'polymorphic_identity': 'TexteQuestion',
        'with_polymorphic': '*',
        "polymorphic_load": "inline"
    }


class MultipleQuestion(Question):
    first_Alternative = db.Column(db.String(120))
    second_Alternative = db.Column(db.String(120))
    third_Alternative = db.Column(db.String(120))
    fourth_Alternative = db.Column(db.String(120))

    def json_content(self):
        json_quest = dict()
        json_quest['firstAlternative'] = self.first_Alternative
        json_quest['secondAlternative'] = self.second_Alternative
        json_quest['thirdAlternative'] = self.third_Alternative
        json_quest['fourthAlternative'] = self.fourth_Alternative
        return json_quest
    __mapper_args__ = {
        'polymorphic_identity': 'MultipleQuestion',
        'with_polymorphic': '*',
        "polymorphic_load": "inline"
    }
