from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'SecretCode'

@app.route('/')
def index():
    if session ['number'] == 0:
        session['number'] = random.randint(1,3)
        print 'I am changing the number right now'
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = request.form['guess']
    if session['guess'] == session['number']:
        session['hint'] = session['guess'], "was the number!"
    elif session['guess'] < session['number']:
        session['hint'] = session['guess'], "is too low!"
    elif session['guess'] > session['number']:
        session['hint'] = session['guess'], "is too high!"
    return redirect('/')

@app.route('/clear')
def clear():
    session.clear()
    session ['number'] = 0
    return redirect('/')

app.run(debug=True)
