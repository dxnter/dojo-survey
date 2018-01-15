from flask import Flask, render_template, request, redirect, session, flash, url_for
app = Flask(__name__)
app.secret_key = 'Dojo'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    error = False

    if len(request.form['name']) < 1:
        flash('Please enter a name!')
        error = True
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']

    if len(request.form['comment']) > 120:
        flash("Comment cannot exceed 120 characters!")
        error = True
    elif len(request.form['comment']) < 1:
        flash('Comment cannot be blank')
        error = True
    else:
        session['comment'] = request.form['comment']
    if error:
        return redirect('/')
    else:
        return render_template('result.html', name=session['name'], location=session['location'], language=session['location'], comment=session['comment'])
app.run(debug=True)