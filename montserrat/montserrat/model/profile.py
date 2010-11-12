# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="maguire"

from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, Unicode
from montserrat.model.meta import Base

class Profile(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('scholar.id'))
    picture_id = Column(Integer, ForeignKey('media.id'))
    school_id = Column(Integer, ForeignKey('school.id'))
    major = Column(Unicode(100))
    gpa = Column(Unicode(10))

    def __init__(self, user, picture=False, school=False, major="", gpa=""):
        self.user_id = user.id
        self.picture_id = picture.id if picture else ""
        self.school_id = school.id if school else ""
        self.major = major 
        self.gpa = gpa
