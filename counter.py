from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)  
app.secret_key = "It's a secret"

@app.route('/')
def counter():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1
    return render_template('index.html')

@app.route('/destroy_session')
def destroy():
    session['count'] = 0
    return redirect('/')

@app.route('/plus_two')
def plus_two():
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 2
    return render_template('index.html')

@app.route('/increment', methods=['POST'])
def increment():
    if request.method == 'POST':
        if request.form['number'] == "":
            return redirect('/chooseamount')
        session['increase'] = request.form['number']
        amount = session['increase']
        num = int(session['count'])
        num += int(amount)
        session['count'] = num
    return redirect('/chooseamount')

@app.route('/chooseamount')
def youchoose():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)