from api.models import db, User
from werkzeug.security import check_password_hash

def exist(email):
    user = User.query.filter_by(email=email).first()
    return user

def createUser(email, password):
    new_user = User(email=email, password=password, is_active=True)
    db.session.add(new_user)
    db.session.commit()
    
    return new_user

