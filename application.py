from flask import Flask, render_template, redirect, url_for
from wtform_fields import *
from models import *

#Configure app

app = Flask(__name__)
app.secret_key = 'replace later'

#Configure DB

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://whhdvebgzlrznh:8fec8b6146aa02b5a0ae33e8777627b77d5d68664a9ac2a0832af537f87bf0ac@ec2-18-234-17-166.compute-1.amazonaws.com:5432/d8j04q3tgjm4d4'

db = SQLAlchemy(app)

@app.route("/", methods=['GET', 'POST'])
def index():

    reg_form = RegistrationForm()
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template("index.html", form=reg_form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    # Permite loguear al usuario si la validacion fue correcta
    if login_form.validate_on_submit():
        return "Estas In!"

    return render_template("login.html", form=login_form)

if __name__ == "__main__":
    app.run(debug=True)


