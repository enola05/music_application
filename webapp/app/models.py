from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db
from app import login,app
from hashlib import md5
from datetime import datetime

class registration(UserMixin,db.Model):
    __tablename__='registration'
    id=db.Column(db.Integer(),primary_key=True)
    username=db.Column(db.String(),nullable=False)
    email=db.Column(db.String(),nullable=False)
    contact=db.Column(db.String())
    password_hash=db.Column(db.String())
    last_seen=db.Column(db.DateTime,default=datetime.utcnow)
    '''def __init__(self,username,contact,password,email):
        self.username=username
        self.contact=contact
        self.password=generate_password_hash(password,method='sha256')
        self.password=password
        self.email=email
    def __repr__(self):
        return f"<result:{self.user_id}>"
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)'''
    def __repr__(self):
        return '<registration {}>'.format(self.username)
    def set_password(self,password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    def avatar(self,size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

@login.user_loader
def load_user(id):
    return registration.query.get(int(id))
