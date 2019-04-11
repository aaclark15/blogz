from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:lc101@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'hjU898lP1'

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(255))

    def __init__(self, title, body): 
        self.title = title
        self.body = body

@app.route('/blog', methods=['POST', 'GET'])
def index(): 
    
    blogs = Blog.query.all()

    return render_template('blog_list.html', title = "Build-A-Blog App", 
        blogs = blogs) 


@app.route('/newpost', methods=['POST', 'GET'])
def add_blog():
    if request.method == 'POST': 
        title = request.form['title']
        body = request.form['body']

        if title != "" and body != "": 
            new_blog = Blog(title, body)
            db.session.add(new_blog)
            db.session.commit()

            return redirect('/blog')
        
        else: 
            flash("Blog post cannot be empty", 'error')
    
    return render_template('newpost.html')


if __name__ == '__main__':
    app.run()