from flask import render_template, redirect, url_for, flash, request
from expovision import app, db, bcrypt
from flask_login import login_user, logout_user, current_user, login_required
from expovision.models import User

@app.route('/')
def index():
    return render_template('index.html')

#ImmutableMultiDict([('text', 'asdf'), ('call', '89292660205'), ('enail', 'wer@mail.ru')])
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated: 
        return redirect(url_for('index'))
    if request.form:
        #hashed_password = bcrypt.generate_password_hash(request.form.get("password")).decode('utf-8')
        #user = User(username=request.form.get("name"), email=request.form.get("email"), password=hashed_password)
        user = User(name=request.form.get("name"), email=request.form.get("email"), phone=request.form.get("phone"))
        db.session.add(user)
        db.session.commit()
        flash(f'Аккаунт  создан {request.form.get("name")}! Вы можете войти в свой аккаунт!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html')



@app.route('/rating', methods=['GET', 'POST'])
def raiting():
    return render_template('rating.html')


@app.route('/lessons', methods=['GET', 'POST'])
def lessons():
    return render_template('lessons.html')


@app.route('/cabinet', methods=['GET', 'POST'])
def cabinet():
    return render_template('cabinet.html')


@app.route('/cabinet-person', methods=['GET', 'POST'])
def cabinet_person():
    return render_template('cabinet.html')
