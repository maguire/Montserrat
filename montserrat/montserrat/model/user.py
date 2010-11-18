# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="maguire"

import hashlib

from sqlalchemy import Column, ForeignKey, orm
from sqlalchemy.types import Integer, Unicode, DateTime, String
from montserrat.model.meta import Base
from montserrat.model.profile import Profile
from montserrat.lib.base import Session 
from datetime import datetime

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    firstname = Column(Unicode(100))
    lastname = Column(Unicode(100))
    username = Column(Unicode(100), unique=True)
    email = Column(Unicode(150), unique=True)
    password = Column(Unicode(32))
    joindate = Column(DateTime)
    user_type = Column(String(20), nullable=False)

    __mapper_args__ = {'polymorphic_on': user_type}

    def __init__(self, firstname, lastname, username, email, password, user_type):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.password = password
        self.user_type = user_type
        self.joindate = datetime.now()  

    @classmethod
    def by_name(cls,username):
        try:
            user = Session.query(cls).filter(cls.username==username).one()
        except orm.exc.NoResultFound:
            return False
        return user
    
    @classmethod
    def by_id(cls,user_id):
        try:
            user = Session.query(cls).filter(cls.id==user_id).one()
        except orm.exc.NoResultFound:
            return False
        return user

class ScholarUser(User):
    __tablename__ = 'scholar'
    __mapper_args__ = {'polymorphic_identity': 'scholar'}
    
    id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    
    def __init__(self, firstname, lastname, username, email, password):
        super(ScholarUser, self).__init__(firstname, lastname, username, email, password, "scholar")

class DonorUser(User):
    __tablename__ = 'donor' 
    __mapper_args__ = {'polymorphic_identity': 'donor'} 
   
    id = Column(Integer, ForeignKey('user.id'), primary_key=True)

    def __init__(self, firstname, lastname, username, email, password):
        super(DonorUser, self).__init__(firstname, lastname, username, email, password, "donor")

def create_user(user_type, user_dict):
    
    user_dict["password"] = hashlib.md5(user_dict["password"]).hexdigest()
    if user_type == "scholar":
        new_user = ScholarUser(**user_dict)
        #create an empty profile and add it to the db
    else :
        new_user = DonorUser(**user_dict)
    Session.add(new_user)
    Session.commit()

    #new_user does not have a user id until after commit
    if user_type == "scholar":
        Session.add(Profile(new_user))
        Session.commit()
    return new_user

def valid_login(email, password):
    password = hashlib.md5(password).hexdigest()
    try:
        user = Session.query(User).filter(User.email==email).\
                filter(User.password==password).one()
    except:
        user = False
    return user

