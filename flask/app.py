from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String(200), nullable = False)
    desc = db.Column(db.String(500), nullable = False)
    dateCreated = db.Column(db.DateTime, default = datetime.utcnow)


    def __repr__(self)->str:
        return f"{self.sno} - {self.title}"


@app.route('/', methods = ['GET', 'POST'])
def home_page():
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']

        todo = Todo(title = title, desc = desc)
        db.session.add(todo)
        db.session.commit()

    alltodo = Todo.query.all()
    print(alltodo)
    return render_template('index.html', alltodo = alltodo)
    # return 'Hello World'

@app.route('/show')
def products():
    alltodo = Todo.query.all()
    print(alltodo)
    return 'This is products page'

if __name__ == "__main__":
    app.run(debug=True, port = 8000)