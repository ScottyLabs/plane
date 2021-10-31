import requests
import os
import webbrowser
import time
from email import utils

from cli import prompt_confirm, prompt_subject, prompt_date, prompt_confirmDate
from util import convert_StrtoDate, returnNewDate

class PlaneSendBase():

    def __init__(self, profile):
        self.domain = profile.domain
        self.api_key = profile.api_key
        self.sender = profile.sender
        self.recepients = profile.recepients
        self.reply_to = profile.reply_to or profile.sender

        self.path_root = 'html'
        self.path_render = f'{self.path_root}/plane-render.html'
        self.shell = open(f'{self.path_root}/shell.html', 'r').read()  # TODO: rename shell

    def __send(self, subject, html, deliverytime):
        return requests.post(
            f"https://api.mailgun.net/v3/{self.domain}/messages",
            auth=("api", self.api_key),
            data={
                "from": self.sender,
                "to": self.recepients,
                'h:Reply-To': self.reply_to,
                "subject": subject,
                "html": html,
                "o:deliverytime": self._format_datetime(deliverytime),
            }
        )

    def populate(self, s, kv):
        '''
        Replace occurences of keys in kv in s with values in kv
        '''
        for placeholder, replacement in kv.items():
            s = s.replace(placeholder, replacement)
        return s

    def edit(self, path):
        os.system('vim ' + os.path.realpath(path))
        return open(path, 'r').read() 

    def stitch(self, body):
        '''
        Takes in the body to put inside shell and generate plane_render.html
        '''
        populated_shell = self.populate(self.shell, {'{plane_body}': body})
        preview = open(self.path_render, 'w+')
        preview.write(populated_shell)
        preview.close()

    def preview(self):
        webbrowser.open_new_tab("file://" + os.path.realpath(self.path_render))
        confirm = prompt_confirm("Does the preview look okay?")
        return confirm

    def _format_datetime(self, dt):
        '''
        Returns date formatted in RFC2822 Format
        '''
        tuple = dt.timetuple()
        timestamp = time.mktime(tuple)
        return utils.formatdate(timestamp)

class PlaneSend(PlaneSendBase):

    def __init__(self, schema, profile):
        super().__init__(profile)
        self.subject = schema.subject or prompt_subject()
        if prompt_confirmDate(schema.delivery_day) == False:
            new_date = prompt_date()
            #convert new_date to int
            int_date = convert_StrtoDate(new_date)
            input_date = returnNewDate(schema.delivery_day, int_date)
            print(input_date, 'input_date')
            print(schema.delivery_day, 'default_date')
            self.delivery_day = input_date
            print(self.delivery_day)
        else:
            self.delivery_day = schema.delivery_day
        
        self.kv = self._get_meeting_kv(schema.meetings) 
        self.id = f'{self.path_root}/{schema.template}' 
        self.path_body = f'{self.id}/body.html'
        self.path_content = f'{self.id}/content.html'
        self.path_default = f'{self.id}/default.html'
        self.path_backup = f'{self.id}/backup.html'

    def execute(self):
        # Restore
        self._restore()
        # Populate
        self._populate()
        
        confirm = False
        while not confirm:
            # Edit
            edited_content = self.edit(self.path_content)
            # Stitch
            body = open(self.path_body, 'r').read()
            populated_body = self.populate(body, {'{plane_content}': edited_content})
            self.stitch(populated_body)
            # Preview
            confirm = self.preview()

        # Send
        html = open(self.path_render, 'r').read()
        response = self._PlaneSendBase__send(self.subject, html, self.delivery_day)
        if response.status_code == 200:
            print("The email has been sent! ✈️")
        else:
            print(response.text)

    def _get_meeting_kv(self, meetings):
        '''
        Generate kv from meetings to pass into the populate method
        '''
        kv = dict()
        if meetings is None: return kv
        for prefix, meeting in meetings.items():
            for suffix, value in zip(meeting._fields, meeting):
                placeholder = f'{{{prefix}_{suffix}}}'
                kv[placeholder] = value
        return kv

    def _restore(self):
        '''
        Restore contents of path_content using path_default and save previous version to path_backup
        '''
        os.system(f"cp {os.path.realpath(self.path_content)} {os.path.realpath(self.path_backup)}")
        os.system(f"cp {os.path.realpath(self.path_default)} {os.path.realpath(self.path_content)}")

    def _populate(self):
        '''
        Populate content file with kv details and save changes
        '''
        fh = open(self.path_content, 'r+')
        content = fh.read()
        populated_content = self.populate(content, self.kv)
        fh.seek(0)
        fh.write(populated_content)
        fh.close()


