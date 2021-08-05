from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)


class Beauty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    pictures = db.Column(db.PickleType(), nullable=False)
    likes = db.Column(db.Integer)
    comments = db.Column(db.Integer)
    number = db.Column(db.Integer)
    gender = db.Column(db.String)

    def __repr__(self):
        return self.description+'\n讚數:'+str(self.likes)


logo = 'https://scontent.ftpe2-1.fna.fbcdn.net/v/t1.6435-1/cp0/p50x50/170337104_101007188787091_7737244323027785300_n.png?_nc_cat=105&ccb=1-3&_nc_sid=dbb9e7&efg=eyJpIjoiYiJ9&_nc_ohc=wcvz5c3WUxcAX-UPqJN&_nc_ht=scontent.ftpe2-1.fna&oh=34de2b0ed211e17947a9efeb090f6ee4&oe=6131D457'


@app.route('/')
def index():
    global logo
    return render_template('index.html', pic=logo)


@app.route('/randpick')
def randpick():
    global logo
    rand_index = random.randint(0, 1)
    logo = Beauty.query.all()[0].pictures[rand_index]
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
