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


def prompt_date():
   dates = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
   questions = [
            {
                'type': 'list',
                'name': 'date',
                'message': 'On which day would you like to send the email?',
                'choices' : dates
            }
       ]
   answers = prompt(questions)
   return answers['date']


def prompt_defaultDateTime(delivery_date):
    questions = [
            {
                'type' : 'confirm',
                'name' : 'confirm',
                'message' : f'Do you want to send this email on {delivery_date} ?',
            }
        ]
    answers = prompt(questions)
    return answers['confirm']



def prompt_confirmDate(delivery_date):
    date = delivery_date.strftime("%A")
    questions = [
            {
                'type' : 'confirm',
                'name' : 'confirm',
                'message' : f'Do you want to send this email on' + ' ' + date + '?',
            }
        ]
    answers = prompt(questions)
    return answers['confirm']

def prompt_shour(message="Are you fine with sending the email at 11 PM?"): 
    # we ask the user if they want to send the email at 11
    # and then this returns a bool corresponding with their answer
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
    # we ask the user what time they want to send the email
    questions = [
        {
            'type': 'input',
            'name': 'hour',
            'message': 'What hour do you want to send the email?'
        }
    ]
    answers = prompt(questions)
    return answers['hour']
