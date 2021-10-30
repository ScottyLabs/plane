from PyInquirer import prompt

from schema import schema
from profiles import profiles


def prompt_schema():
    questions = [
        {
            'type': 'list',
            'name': 'schema',
            'message': "What type of email do you want to send?",
            'choices': [ ps.id for ps in schema ],
        }
    ]
    answers = prompt(questions)

    for ps in schema:
        if ps.id == answers['schema']:
            return ps


def prompt_profile():
    # return profiles[1] # TODO: remove hardcode testing
    questions = [
        {
            'type': 'list',
            'name': 'profile',
            'message': "Which profile do you want to use?",
            'choices': [ profile.id for profile in profiles ],
        }
    ]
    answers = prompt(questions)
    
    for profile in profiles:
        if profile.id == answers['profile']:
            return profile


def prompt_confirm(message="Do you want to confirm?"):
    questions = [
        {
            'type': 'confirm',
            'name': 'confirm',
            'message': message,
        }
    ]
    answers = prompt(questions)
    return answers['confirm']


def prompt_subject():
    questions = [
        {
            'type': 'input',
            'name': 'subject',
            'message': "What is the subject of the email?",
        }
    ]
    answers = prompt(questions)
    return answers['subject']


def prompt_shour(message="Are you fine with sending the email at 11 PM?"): 
    questions = [
        {
            'type': 'confirm',
            'name': 'confirm',
            'message': message,
        }
    ]
    answers = prompt(questions)
    return answers['confirm']


def prompt_hour(): 
    questions = [
        {
            'type': 'input',
            'name': 'hour',
            'message': 'What hour do you want to send the email?'
        }
    ]
    answers = prompt(questions)
    return answers['hour']
