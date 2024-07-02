from flask import render_template, redirect, url_for, request

from app.main import bp
from app.models.user import User

from app.extensions import db

@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/success/<name>/<password>')
def success(name, password):
    return 'Hello %s, this is the password %s' % (name, password)

# The login url should be presented on your laptop by the URL
# http://localhost:5000/login
@bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['user']
        return redirect(url_for('main.success', name=user, password="mygreatpassword"))
    else:
        return render_template('login.html')

# The register url should be presented on your laptop by the URL
# http://localhost:5000/register
@bp.route('/register', methods=(['POST', 'GET']))
def register():
    if request.method == 'POST':
        new_user = request.form['user']
        existing_users = User.query.all()
        found = False 
        for user in existing_users:
            print(user.username)
            if user.username == new_user:
                found = True
                print("Found user " + user.username)

        if not found:
            create_user = User(new_user)
            db.session.add(create_user)
            db.session.commit()
        else:
            print("User already registered")
        return redirect(url_for('main.success', name=user.username, password=user.password))
    else:
        return render_template('register.html')

