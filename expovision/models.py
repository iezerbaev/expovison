from expovision import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    #username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    phone = db.Column(db.String(12), nullable=False, unique=True)
    #avatar = db.Column(db.String(20), nullable=False, default='default.jpg')
    
    #password = db.Column(db.String(20), nullable=False)
    

    def __repr__(self):
        return self.username