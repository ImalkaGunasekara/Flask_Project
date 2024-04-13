from flask import Flask, render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# let's set up our application

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default= datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id






# let's add the app route decorator

@app.route('/')
def index():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True) #This will pop up any error in the web page


