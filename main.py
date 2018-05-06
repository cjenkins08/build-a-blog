from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:2008@localhost:3306/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(120))

    def __init__(self, title, body):
        self.title = title
        self.body = body

@app.route('/blog', methods=['POST', 'GET'])
def allblogs():
    blogs = Blog.query.all()
    

    blog_value = request.args.get('id')
    if blog_value: 
        blogs = Blog.query.get(blog_value)
        return render_template('individual.html', blogs = blogs)
    return render_template("mainblog.html", blogs=blogs)


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

    

newblog = []

@app.route('/newblog', methods=['POST', 'GET'])
def new():


    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        errormsg = ''

        if title == '' or body == '':
            errormsg = "You gave me an empty blog. Try again!"
            return render_template('newblog.html', errormsg =errormsg)
        else:
             title = request.form['title']
             body = request.form['body']
             individual = Blog(title,body)

             db.session.add(individual)
             db.session.commit()
             return redirect('/blog')
             
    return render_template('newblog.html')




        






#link needed redirect to the new blog page if the button is selected
if __name__ == '__main__':
    app.run()