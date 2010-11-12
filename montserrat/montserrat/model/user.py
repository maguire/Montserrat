# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="maguire"

from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, Unicode, DateTime, String
from montserrat.model.meta import Base
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


