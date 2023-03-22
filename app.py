from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres123@localhost/height_collector'
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(100), unique=True)
    height_ = db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():
    if request.method == "POST":
        email = request.form["email_name"]
        height = request.form["height_name"]
        send_email(email, height)

        if db.session.query(Data).filter(Data.email_ == email).count() == 0:
            data = Data(email, height)
            db.session.add(data)
            db.session.commit()
            return render_template("result.html")

        return render_template("index.html", text="seems like we have got something from the email address already!")


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.debug = True
        app.run()
