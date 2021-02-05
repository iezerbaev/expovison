from expovision import db

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    #avatar = db.Column(db.String(20), nullable=False, default='default.jpg')
    #phone ?
    password = db.Column(db.String(20), nullable=False)
    

    def __repr__(self):
        return self.username