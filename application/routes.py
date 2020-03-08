from application import app
from flask import render_template,url_for,request,redirect
import sqlite3

# @app.route('/')
@app.route('/home')
@app.route('/index') 
def index():
    return render_template('index.html',index=True)

@app.route('/courses/')
@app.route('/courses/<term>')
def courses(term='Spring 2030'):
    courseDataa = [{"courseID":"1111","title":"PHP 111","description":"Intro to PHP","credits":"3","term":"Fall, Spring"}, {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":"4","term":"Spring"}, {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":"3","term":"Fall"}, {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":"3","term":"Fall, Spring"}, {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":"4","term":"Fall"}]
    # print(courseData[1]['title'])
    return render_template('courses.html',courseData=courseDataa,courses=True,term=term)

@app.route('/login')
def login():
    return render_template('login.html',login=True)

@app.route('/register')
def register():
    return render_template('register.html',register=True)


'''

@app.route('/login',methods=['POST'])
def login():
    return 'Login'

@app.route('/About')
def about():
    return (url_for('index'))    

'''

@app.route('/pre',methods=['POST','GET'])
def pre():
    if request.method == 'GET':
        return render_template('req.html')         
    elif request.method == 'POST':
        fn = request.form
        return fn
#upload a file in flask
@app.route('/test',methods=['POST','GET'])
def upload_file():
    if request.method == 'GET':
        return render_template('upload.html')         
    elif request.method == 'POST':
        f=request.files['image']
        f.save('image_uploaded/'+f.filename)
        return redirect('/test')


#give data from user and send that to db
@app.route('/')
def post():
    return render_template('post.html')
@app.route('/save',methods=['POST','GET'])
def save():
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    title = request.form['Title']
    body = request.form['Body']
    cur.execute("INSERT INTO Post(Title,Body) VALUES('{0}','{1}')".format(title,body))
    conn.commit()
    conn.close()
    return redirect('/')



#request in flask

@app.route('/kavehtest/')
def request_get():

    name=request.args.get('name','Omid')
    return name   

        


