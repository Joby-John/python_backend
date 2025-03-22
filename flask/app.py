from flask import Flask, render_template
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


@app.route('/')
def home_page():
    todo = Todo(title = "Learn Python web Dev", desc = "Flask, Django, Mongo")
    db.session.add(todo)
    db.session.commit()
    return render_template('index.html')
    # return 'Hello World'

@app.route('/products')
def products():
    return 'This is products page'

if __name__ == "__main__":
    app.run(debug=True, port = 8000)