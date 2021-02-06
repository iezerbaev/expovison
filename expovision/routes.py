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
    email = User.query.filter_by(email=request.form.get("email")).first()
    username = User.query.filter_by(username=request.form.get("username")).first()
    phone = User.query.filter_by(phone=request.form.get("phone")).first()
    if username:
        return flash(f'Имя пользователя, занято!', 'danger')
    elif email:
        return flash(f'Такая почта уже есть в базе!', 'danger')
    elif phone:
        return flash(f'Номер телфона уже есть в базе!', 'danger')
    elif request.form.get("password") != request.form.get("confirm_password"):
        return flash(f'Пароли не совподают', 'danger')
    if request.form:
        hashed_password = bcrypt.generate_password_hash(request.form.get("password")).decode('utf-8')
        user = User(username=request.form.get("username"), email=request.form.get("email"), phone=request.form.get("phone"), password=hashed_password, fio='fio')
        db.session.add(user)
        db.session.commit()
        flash(f'Аккаунт  создан {request.form.get("username")}! Вы можете войти в свой аккаунт!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated: 
        return redirect(url_for('index'))
    if request.form.get('email'):
        user = User.query.filter_by(email=request.form.get('email')).first()
        if user and bcrypt.check_password_hash(user.password, request.form.get('password')):
            login_user(user, remember=False)
            return redirect(url_for('index'))
        else:
            flash('Не правильный email или пароль', 'danger')
    return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/rating', methods=['GET', 'POST'])
def raiting():
    users = User.query.order_by(User.rating.desc()).all()
    return render_template('rating.html', users=users)


@app.route('/lessons', methods=['GET', 'POST'])
def lessons():
    return render_template('lessons.html')


@app.route('/cabinet', methods=['GET', 'POST'])
def cabinet():
    return render_template('cabinet.html')


@app.route('/cabinet-person', methods=['GET', 'POST'])
def cabinet_person():
    return render_template('cabinet-person.html')
