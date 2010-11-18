# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="maguire"

from sqlalchemy import Column, ForeignKey, orm
from sqlalchemy.types import Integer, Unicode
from montserrat.model.meta import Base
from montserrat.lib.base import Session

class Profile(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('scholar.id'))
    picture_id = Column(Integer, ForeignKey('media.id'))
    school_id = Column(Integer, ForeignKey('school.id'))
    major = Column(Unicode(100))
    gpa = Column(Unicode(10))

    def __init__(self, user):
        self.user_id = user.id

    @classmethod
    def by_user_id(cls, user_id):
        try:
            profile = Session.query(cls).filter(cls.user_id==user_id).one()
        except orm.exc.NoResultFound:
            profile = False
        return profile
