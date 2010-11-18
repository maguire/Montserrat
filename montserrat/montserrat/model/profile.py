# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="maguire"

from sqlalchemy import Column, ForeignKey, orm
from sqlalchemy.orm import relation
from sqlalchemy.types import Integer, Unicode, DateTime
from montserrat.model.meta import Base
from montserrat.lib.base import Session
from montserrat.model.user import User, ScholarUser, DonorUser
from montserrat.model.school import School
from montserrat.model.media import Media

class Profile(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relation(ScholarUser, uselist=False, backref='user')
    picture_id = Column(Integer, ForeignKey('media.id'))
    picture = relation(Media, uselist=False, backref='media')
    school_id = Column(Integer, ForeignKey('school.id'))
    school = relation(School, uselist=False, backref='school')
    #race_id = Column(Integer, ForeignKey('race.id'))
    #religion_id = Column(Integer, ForeignKey('religion.id))
    birthdate= Column(DateTime)
    hometown = Column(Unicode(100))
    major = Column(Unicode(100))
    gpa = Column(Unicode(10))

    def __init__(self, user):
        self.user = user

    @classmethod
    def by_user_id(cls, user_id):
        try:
            profile = Session.query(cls).filter(cls.user_id==user_id).one()
        except orm.exc.NoResultFound:
            profile = False
        return profile
