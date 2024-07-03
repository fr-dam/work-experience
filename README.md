# Login Application


## Objective
You are going to create a Python Flask application that will authenticate a user and give them access to a few simple web-pages.

The objective here is to look at the authentication part of writing an application.


> ### Important! 
>These instructions weren't written for Windows. You may need to edit some of the directory paths to a `\` instead of `/`. You may
> also need to add `.exe` to the end of the commands for sqlite3 (i.e. `sqlite3.exe`)

## Prerequisites
1. To make sure that you have the relevant software installed first of all install Python using [these instructions](https://realpython.com/installing-python/)
2. Install the packages required to write your Flask app by following [these instructions](#dependencies)
3. Install sqlite3 which you will need to view and update the SQL database, [instructions](https://www.tutorialspoint.com/sqlite/sqlite_installation.htm)
4. Install git which you will use to make your changes, [instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
5. Clone the repo `https://github.com/fr-dam/work-experience` to your local machine, [instructions](#checking-out-a-repo)
6. Make sure you a code editor installed on your laptop, here's a link to a [popular free editor](https://code.visualstudio.com/download)

> ### Important! 
> You will likely need to update your PATH environment variable to allow your system to find the executable files for your
> sqlite installation and also the python libraries installed with pip. There are some instructions [here](https://www.computerhope.com/issues/ch000549.htm)
> but ask for help if it's not something you're familiar with.

## Background
Before you begin, here's a list of the files we've provided:

```
├── app
│   ├── extensions.py
│   ├── __init__.py
│   ├── main
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── models
│   │   └── user.py
│   └── templates
│             ├── base.html
│             ├── index.html
│             ├── login.html
│             └── register.html
└── config.py
```

`config.py`:
    This loads the database `app.db` which is used to store user details (id, username and password). You shouldn't need to edit this file
`extensions.py`:
    This loads the SQLAlchemy library to help us talk to the sqlite database. This is really just a framework that makes it easier to talk to a database.
Files under `app/templates`:
    These are what is shown in the browser and are a type of HTML template. They are able to inherit
    content (in our example from `base.html`) which is mostly rendering the menu bar at the top of each 
    page.
`app/main/routes.py`:
    is where the logic goes, you'll probably spend most of your time editing this file. It has 3 methods currently (login, register and success) which are mapped to the URL path specified by 
    `@bp.route('/login', methods=['POST', 'GET'])` where `/login` is the path after the URL. The register method is where we've put most of the logic which allows new users to register. 

Most of the structure and basic configuration were taken from [here](https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy) if you want to see a more in depth set of instructions

### Preparation
Once you have installed Flask and the other dependencies you will need to initialise the database. Most of this is handled for you by SQLAlchemy but you will need to run the following commands in a terminal

```
cd <path to repo>/auth_app/
flask shell
```

This will take you into an interactive Python (Flask) shell. From there run these commands:

```
from app.extensions import db 
db.create_all()
<Ctrl-D>
```

This should create a `user` table with the structure defined in `app/models/user.py`. To confirm this and get you started run the following:
The last shortcut `Ctrl-D` will exit the Flask shell. You should now have a file called app.db which is where sqlite will store your users

```
cd <path to repo>/auth_app
sqlite3 app.db
# You don't need to type `sqlite>` at the begining of the following lines, it's the prompt sqlite displays
sqlite> .schema user
sqlite> INSERT INTO user (username, password) VALUES ('bob','Password1');
sqlite> SELECT * FROM user;
1|bob|Password1
```

Here's a [useful tutorial](https://www.tutorialspoint.com/sqlite/sqlite_insert_query.htm) on sqlite

Now we're going to test the existing application. Make sure you're in the `auth_app` directory. Run the following command:

```
flask run
```
This should startup up the application. Go to your browser and type `http://localhost:5000/login` into the address bar. This should take you
to the login page for our app.

Type your name into the text box and hit submit.

### Tasks
We don't expect you to get to the end of this list of tasks (although it's fantastic if you do). We've tried to include enough content to keep you occupied for the whole day.

1. Change the login page (app/templates/login.html) and function (app/main/routes.py) to request a password as well as a username and check that the user/password are correct (it's ok to hard code the username/password to begin with). 
2. Change the login function to read from the database (see the register function to get you started) and check that the username/password exists in the db.  
3. If the user doesn't exist or the password is wrong show an appropriate error message in the browser.
4. Currently, the app only asks for a username when registering a user. Add another field to `app/templates/register.html` to include a password text field.
5. Edit `app/main/routes.py` to store the password as well as the username on line 37.
6. If the user is already found in the database make the app update their password if they use the 
register URL. Currently is just prints a message to say they are already registered before going to the `success` endpoint.
To do this you will have to create a new html page with a form which just asks for the password. You will probably need to store the username
in a hidden form field otherwise you won't have the username
7. Customise the HTML templates under `app/templates` to make them more interesting. You could try a variety of things but it's really up to you. Anything which is valid HTML is great and you should be able to find a lot of tutorials online to help you. Here's an [example](https://www.w3schools.com/html/). Some things you could try:
   * Change the colour of the text for the links in the menu
   * Change the page background colour
   * Add an image
   * Use CSS to format the templates
8. Write a small paragraph which explains the difference between the `POST` and `GET` HTTP methods and what other methods are available as part of the HTTP protocol and when you are likely to use each.
9. Currently, the `success` route doesn't use a HTML template and just prints some raw text out to the browser. Get it to use a template instead, you'll have to add a file (`app/templates/success.html` and get the `success` method to render that instead)
10. In the real world it's a **VERY BAD IDEA** to store passords unencrypted in a database, do some research to say what you could do about this and write a paragraph about it.


#### Checking out a repo
Most developers will have a dedicated directory where the check various repositories to keep them organised. Even if it's just a directory under your "My Documents" or home directory so create 
a folder somewhere and change directory to it. If you're using a terminal, then cd to the directory you created before running the git checkout below.

The following commnand allows you to checkout a repo:

```
git clone https://github.com/fr-dam/work-experience
cd work-experience
```

This will fetch the full contents of that repo including the flask starter app under `work-experience/auth-app`

Once you have the files on your laptop, create a branch to do your work on. You shouldn't commit changes to the master branch.
Replace `my-branch-name` with something that makes more sense.

```
git checkout -b my-branch-name
```

Once you complete a task you can push your changes by running the following git commands:

```
git add -A
git commit -m "Describe what I changed"
git push origin my-branch-name
```

Once you do this your changes will be viewable in the github web user interface.


#### Dependencies
Dependencies are libraries of code that have been developed by other people which make it easier to write complex applications.

You can import these into your python program and use the code they've written to reduce the amount of code you need to write.

We are going to install the following packages using `pip` which is the main Python package installer/manager

```
pip install Flask Flask-SQLAlchemy
```

The last 2 are for working with databases and we may not get that far!

#### Running in a Python Virtual Environment
If you want to run this without installing the python modules globally on your machine, you can run it in a virtual environment
which stores python binaries and modules locally within your project directory.

```
cd <path to repo>
python -m venv  <path to repo>
cd auth_app
../bin/pip install Flask Flask-SQLAlchemy
../bin/flask run 

```

You may have to change the above paths if you are running on Windows.