from .app import app,db
from .models import Questionnaire, Question, SimpleQuestion, MultipleQuestion

@app.cli.command()
def syncdb():
    "Creation de la bd"
    db.create_all()
"""
questionnaires = [
    {"name": "Questionnaire_1",
        "questions": [{
            'title': 'Quelle est la capitale de la France ?',
            'question_type': 'SimpleQuestion',
            'firstAlternative': 'Paris',
            'secondAlternative': "Marseille",
            "firstChecked": "true"
        },
            {
            'title': 'Quelle est le pays le plus grand du monde',
            'question_type': 'SimpleQuestion',
            'firstAlternative': 'Kazakhstan',
            'secondAlternative': "Russie",
            "firstChecked": "false"

        },
            {
            'title': "Quelle est la capitale de l'Espagne ?",
            'question_type': 'RadioQuestion',
            'reponse1': 'Varsovie',
            'reponse2': 'Madrid',
            'reponse3': 'Lisbonne',
            'reponse4': 'Barcelone',
            'reponse_true': 2

        },
        {
            'title': "Combien de coupe du monde a remporté l'équipe de France de football ?",
            'question_type': 'NumericQuestion',
            'reponse': 2
        },
        ]
     },
]
"""

questionnaires = [
    {"name": "Questionnaire_1",
        "questions": [{
            'title': 'Quelle est la capitale de la France ?',
            'question_type': 'SimpleQuestion',
            'firstAlternative': 'Paris',
            'secondAlternative': "Marseille",
            "firstChecked": "true"
        },
            {
            'title': 'Quelle est le pays le plus grand du monde',
            'question_type': 'SimpleQuestion',
            'firstAlternative': 'Kazakhstan',
            'secondAlternative': "Russie",
            "firstChecked": "false"

        },
        {
            'title': 'Qui est le meilleur ?',
            'question_type': 'MultipleQuestion',
            'firstAlternative': 'Teemo',
            'secondAlternative': "Garen",
            'thirdAlternative': 'Ryze',
            'fourthAlternative': "Moi",
        },
        ]
     },
     {"name": "Questionnaire_2",
        "questions": [{
            "title": "Quelle est la capitale de l'angleterre ?",
            'question_type': 'SimpleQuestion',
            'firstAlternative': 'Paris',
            'secondAlternative': "Londre",
            "firstChecked": "true"
        },
            {
            'title': 'Quelle est le pays le plus petit du monde',
            'question_type': 'MultipleQuestion',
            'firstAlternative': 'Kazakhstan',
            'secondAlternative': "Russie",
            'thirdAlternative': 'Le Vatican',
            'fourthAlternative': "Le Japon",

        },
        {
            'title': 'Qui est le meilleur ?',
            'question_type': 'MultipleQuestion',
            'firstAlternative': 'Teemo',
            'secondAlternative': "Garen",
            'thirdAlternative': 'Ryze',
            'fourthAlternative': "Moi",
        },
        ]
     },
]

@app.cli.command()
def loaddb():
    '''
     Populate tables with data in filename
    '''
    for questionnaire in questionnaires:
        nouveau_questionnaire = Questionnaire(name=questionnaire["name"])
        db.session.add(nouveau_questionnaire)
        db.session.commit()
        for question in questionnaire["questions"]:
            if question["question_type"] == "SimpleQuestion":
                new_question = SimpleQuestion(title=question["title"], question_type=question["question_type"], questionnaire_id=nouveau_questionnaire.id,
                                                 firstAlternative=question["firstAlternative"], secondAlternative=question["secondAlternative"], firstChecked=True if question["firstChecked"] == True else False)
            if question["question_type"] == "MultipleQuestion":
                new_question = MultipleQuestion(title=question["title"], question_type=question["question_type"], questionnaire_id=nouveau_questionnaire.id,
                                                 first_Alternative=question["firstAlternative"], second_Alternative=question["secondAlternative"], 
                                                 third_Alternative=question["thirdAlternative"], fourth_Alternative=question["fourthAlternative"]
                                                 )
            db.session.add(new_question)
    db.session.commit()                                             