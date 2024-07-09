from flask import render_template, redirect, url_for, request

from app.main import bp
from app.models.user import User

from app.extensions import db

@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/success/<name>')
def success(name):
    return 'Hello %s' % name

# The login url should be presented on your laptop by the URL
# http://localhost:5000/login
@bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form["password"]
        if password == "Password1":
            print("The correct password was used " + password)
            isPasswordCorrect = True
        else:
            print("it didnt work try " + password)
            isPasswordCorrect = False   
            return render_template('login.html')
            
        return redirect(url_for('main.success', name=user))
    else:
        return render_template('login.html')



# The register url should be presented on your laptop by the URL
# http://localhost:5000/register
@bp.route('/register', methods=(['POST', 'GET']))
def register():
    if request.method == 'POST':
        new_user = request.form['user']
        new_password = request.form['password']
        existing_users = User.query.all()
        found = False 
        for user in existing_users:
            print(user.username)
            print(user.password)
            if user.username == new_user:
                found = True
                print("Found user " + user.username)
        if not found:
            create_user = User(username = new_user, password = new_password)
            db.session.add(create_user)
            db.session.commit()
            print("User already registered")
        return redirect(url_for('main.success', name=user.username))
    else:
        return render_template('register.html')