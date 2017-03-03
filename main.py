import triggers

from flask import Flask
app = Flask(__name__)

@app.route('/')
def landing():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('main_page.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session['logged_in'] = True
        flash('You were logged in')
        return redirect(url_for('landing'))
    else:
        return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('login'))
