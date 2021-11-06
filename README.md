# Running the program after initial installation
1. In your terminal (Unix/macOS) or command prompt (Windows), cd into the plane folder
2. Run "source env/bin/activate" (Unix/macOs) or ".\env\Scripts\activate" (Windows). This will activate the virtual environment
3. Now, run "python3 plane.py" to begin the program. 
4. Use the arrow keys to move up and down between the available options at each prompt. 
5. Once you select which type of email you want to send, you will see the HTML template for the email in vim. To edit it directly, press "i".
6. Once you are done editing the file, press "esc" and type ":wq". This will save your changes and open up a preview of the email in your browser.
6. Go back to your terminal (Unix/macOS) or command prompt (Windows). To continue editing the file, type "n". To send out the email, enter "y".
    **NOTE**: entering "y" will automatically send out the email.
7. To exit the program at any time, simply press "control + c"
    **NOTE**: be sure to exit out of editing before pressing "control + c"
8. Be sure to deactivate the virtual environment at the end of your session by running "deactivate".


# Creating a new email template (with Zoom links)
1. In schema.py, create a new schema in following the form below:
```
    schema_name = PlaneSchema( 
        'id', # this is what shows up in the options menu 
        'template', 
        'subject', # None if you want to manually input this every time
        f(Day.DELIVERY_DAY), # either Day.DAYOFWEEK or Day.TODAY
        { # set containing the names and meetings of your message
            'new1': m_new1,
            'new2': m_new2,
        },
    )
```
2. Add your schema to the list of schemas at the bottom of the schema.py file

3. In meetings.py, create a new Meeting instance of the form:
```
    m_new = Meeting(
        'name',
        get_next_datetime_formatted(Day.DAY), #either Day.DAYOFWEEK or Day.TODAY
        'location',
    )
```
4. Import your new Meeting instance at the top of the schema.py file

5. Create a new folder for your new email template name under HTML with the following files:
    - body.html # HTML formatting for the email
    - default.html # message body
        - use ```{meeting_name}```, ```{meeting_date}```, and ```{meeting_location}``` respectively
        - example: ```Come to our {new1_name} meeting on {new1_date} at {new1_time} at {meeting_location}```
    - **note:** the content.html and backup.html files will be created/updated every time you run the program

6. Now run plane.py in your terminal (macOS) or your command prompt (Windows) and make sure that your new template is an option!