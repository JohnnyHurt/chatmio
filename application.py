from flask import Flask, render_template
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

        # Check if user exists in DB
        user_object = User.query.filter_by(username=username).first()

        if user_object:
            return "User already registered"

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return "User inserted to the DB"

    return render_template("index.html", form=reg_form)


if __name__ == "__main__":
    app.run(debug=True)


