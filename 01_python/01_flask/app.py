from flask import Flask, render_template , request
from datetime import datetime 
import random

app = Flask(__name__)

@app.route('/')
def hello():
    #return 'Hello World!'
    return render_template('index.html')

@app.route('/t4ir')
def t4ir():
    return 'This is T4IR'

@app.route('/ssafy')
def ssafy():
    return 'SSAFY'


@app.route('/dday')
def dday():
    today = datetime.now()
    end = datetime(2020,4,21)
    td = end-today
    return f'{td.days}일 남았습니다.'

@app.route('/html')
def html():
    return '<h1>This is HTML H1 tag</h1>'

@app.route('/html_line')
def html_line():
    return '''
    <h1>This is HTML H1 tag</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
    '''

@app.route('/greeting/<string:name>')
def greeting(name):
    #return f'반갑습니다! {name}님'
    return  render_template('greeting.html',html_name = name)

@app.route('/cube/<int:number>')
def cube(number):
    #return f'{number}의 3제곱 {number**3}'
    result = number**3
    return render_template('cube.html', result=result, number = number)


@app.route('/lunch/<int:people>')
def lunch(people):
    menu = ['짜장면','탕수육','짬뽕','고추자채밥']
    order = random.sample(menu, people)
    return str(order)


@app.route('/movie')
def movie():
    movies = ['겨울왕국2','나이브스아웃','21','백두산','블랙위도우']
    return render_template('movie.html',movies=movies)

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    age = request.args.get('age')
    return render_template('pong.html', age_in_html=age)

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/google')
def google():
    return render_template('google.html')

@app.route('/isitbirth')
def isitbirth():
    today = datetime.now()
    if today.month == 12 and today.day == 12:
        result = True
    else:
        result = False
    return render_template('isitbirth.html',result=result)


@app.route('/godmademe')
def godmademe():
    name = request.args.get('name')
    first_list = ['잘생김','못생김','어중간']
    second_list = ['자신감','쑥스러움','애교','잘난척']
    third_list = ['허세','돈복','식욕','물욕','성욕']

    first = random.choice(first_list)
    second = random.choice(second_list)
    third = random.choice(third_list)

    return render_template('godmademe.html', name=name, first=first, second=second, third=third)

if __name__=='__main__':
    app.run(debug=True)








