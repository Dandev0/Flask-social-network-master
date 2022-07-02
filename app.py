from flask import Flask, render_template, redirect, request, url_for, flash
from db import avtorisation_login, avtorisation_password, registration_user


app = Flask(__name__)
app.secret_key = "super secret key"

@app.route('/auth', methods = ['POST', 'GET'])
def auth_page():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == avtorisation_login() and password == avtorisation_password():
            return redirect("main", code=302)
        else:
            flash('No valid login or password')
    return render_template('auth.html', error=error)

@app.route('/main')
def main_page():
    return render_template('page.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/')
def default_page():
    return redirect('auth', code=302)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route('/registration', methods = ['POST', 'GET'])
def registration():
    registration_user()
    return render_template('REGISTRATION.html')




if __name__ == "__main__":
    app.run(debug=True)