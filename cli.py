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

#prompt confirmation
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

#Ask the user to input the subject of the email
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

#Ask the user to choose a date to send the email if they do not want to send the email
#at the default date and time
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

#check with the user if they want to send the email at the default date and time
def prompt_defaultDateTime(delivery_date):
    questions = [
            {
                'type' : 'confirm',
                'name' : 'confirm',
                'message' : f'Do you want to send this email on {delivery_date}?',
            }
        ]
    answers = prompt(questions)
    return answers['confirm']



def prompt_hour(): 
    # check with the user on when they would like to send the email 
    questions = [
        {
            'type': 'input',
            'name': 'hour',
            'message': 'When would you like to send the email?'
        }
    ]
    answers = prompt(questions)
    return answers['hour']
