from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@127.0.0.1:5432/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

class Alumni(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    graduation = db.Column(db.String())

    # Debugging use
    def __repr__(self):
        return f'<Person ID: {self.id}, name: {self.name}>'

db.create_all()

newAlumni = Alumni(name='Nichiren', graduation='1222')
db.session.add(newAlumni)
db.session.commit()

@app.route('/')
def index():
    person = Alumni.query.first()
    return 'Hello ' + person.name


if __name__ == '__main__':
    app.run()
