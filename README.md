# Cheat Sheet
Notes from the course.

`postgresql://user:password@localhost:5432/myexample`
1. dialect: postgresql
2. user: a valid user
3. password: a valid password (optional)
4. host: remote or localhost
5. port: default port in this case
6. database: an existing database



~~~
# Hello World Flask App
# Takes a record from DB & Prints

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://udacitystudios@localhost:5432/example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Person(db.Model):
  __tablename__ = 'persons'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False)

db.create_all()

@app.route('/')
def index():
  person = Person.query.first()
  return 'Hello ' + person
~~~






python command interpret this file like main file to run it
~~~
if __name__ == '__main__':
    app.run()
~~~







ORM SQLAlchemy Methods
~~~
$ python3
>>> from flask_hello_app import Person, db
>>> Person.query.all()
>>> Person.query.first()
>>> query = Person.query.filter(Person.name == 'Amy')
>>> query.first()
>>> query.all()
~~~




## Query = SELECT
In SQLAlchemy the SELECT statement is represent by Query method. Example `MyModel.query.all()` selects all from MyModel. If we save this into a variable we could manipulate that data.








//
