from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://2008:build-a-blog@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Task(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    completed = db.Column(db.Boolean)

    def __init__(self, name):
        self.name = name
        self.completed = False

mainblog = []


@app.route('/mainblog', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        mainblog = request.form['mainblog']
        new_blog = mainblog(new_blog)
        db.session.add(new_blog)
        db.session.commit()

    blogs = mainblog.query.filter_by(completed=False).all()
    completed_blogs = mainblog.query.filter_by(completed=True).all()
    return render_template('base.html',title="Let's Build A Blog!", 
        blogs=blogs, completed_blogs=completed_blogs)@app.route('/delete-task', methods=['POST'])


@app.route('/delete-blog', methods=['POST'])
def delete_blog():

    mainblog_id = int(request.form['mainblog-id'])
    mainblog = mainblog.query.get(mainblog_id)
    mainblog_id.completed = True
    db.session.add(mainblog)
    db.session.commit()
...
return redirect('/')

    

newblog = []

@app.route('/newblog', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        newblog = request.form['newblog']
        new_blog = newblog(new_blog)
        db.session.add(new_blog)
        db.session.commit()

    blogs = newblog.query.filter_by(completed=False).all()
    completed_blogs = newblog.query.filter_by(completed=True).all()
    return render_template('base.html',title="Let's Build A Blog!", 
        blogs=blogs, completed_blogs=completed_blogs)


@app.route('/delete-blog', methods=['POST'])
def delete_blog():

    newblog_id = int(request.form['newblog-id'])
    newblog = newblog.query.get(newblog_id)
    newblog_id.completed = True
    db.session.add(newblog)
    db.session.commit()
...
return redirect('/')

#link needed redirect to the new blog page if the button is selected
if __name__ == '__main__':
    app.run()