# Plane Mail Management Initial Documentation

### Onboarding Instructions for Testing on Windows

1. Go to "Turn Windows features on or off" in the control panel

2. Enable "Windows Subsystem for Linux" checkbox. You may have to restart your computer for changes to take effect

3. Install Ubuntu (It's on Microsoft Store).

4. Choose a location and create a folder to store the content for Plane Mail. You can use cd ~ to create the folder in a separate file system from your local drive.

5. Install python 3 and pip if you have not already done so. You can run "sudo apt update" and "sudo apt install python3-pip"

6. Create a virtual environment by running: "python3 -m venv {name}"

7. Activate environment by running: "source {name}/bin/activate"

8. Git clone the repository in the environment you have created (git clone https://github.com/ScottyLabs/plane.git). Move into the new branch you are editing on.

9. Install requirement files by running: "python3 -m pip install -r requirements.txt"

10. cd into the "plane" folder and transfer the file secrets.py into the "plane" folder. You can do this in Command Prompt with "mv ~/(PATH_TO_SECRETS.PY_HERE)/secrets.py ~/(PATH_TO_YOUR_PLANE_DIRECTORY_HERE)/secrets.py". 

11. Run plane.py for testing (You can do this in the plane directory with all the .py files by doing "python3 plane.py" in Command Prompt).

12. You've finished the setup! Whenever you want to access your environment do step 4, then you can cd into your plane folder and run the python files from there.

### Onboarding Instructions for Testing on Mac

1. Create a new folder to store the contents of the Plane Mail Management repository. 

2. In Terminal, cd into the folder you have just created

3. Create a virtual environment by running: "python3 -m venv {name}"

4. Activate environment by running: "source {name}/bin/activate"

5. Git clone the repository in the environment you have created (git clone https://github.com/ScottyLabs/plane.git). Move into the new branch you are editing on

6. Install requirement files by running: "python3 -m pip install -r requirements.txt"

7. cd into the "plane" folder and transfer the file secrets.py into the "plane" folder. You can do this in Terminal with "mv ~/Downloads/secrets.py ~/(PATH_TO_YOUR_PLANE_DIRECTORY_HERE)/secrets.py". 

8. Run plane.py for testing (You can do this in the plane directory with all the .py files by doing "python3 plane.py" in your Terminal).

9. You've finished the setup! Whenever you want to access your environment do step 4, then you can cd into your plane folder and run the python files from there.

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
        'time',
        'Zoom link',
    )
```
4. Import your new Meeting instance at the top of the schema.py file

5. Create a new folder for your new email template name under HTML with the following files:
    - body.html # HTML formatting for the email
    - default.html # message body
        - use ```{meeting_name}```, ```{meeting_date}```, ```{meeting_time}```, ```{meeting_zoom}``` respectively
        - example: ```Come to our {new1_name} meeting on {new1_date} at {new1_time} over <a href="{reminder_zoom}">Zoom</a>!```
    - **note:** the content.html and backup.html files will be created/updated every time you run the program

6. Now run plane.py in your terminal (macOS) or your command prompt (Windows) and make sure that your new template is an option!
