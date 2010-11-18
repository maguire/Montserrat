# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="maguire"

from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, Unicode
from montserrat.model.meta import Base
from montserrat.lib.base import Session

class School(Base):
    __tablename__ = "school"

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(100))
    mail_address = Column(Integer, ForeignKey('address.id'))

    def __init__(self, name, address = None):
        self.name = name
        self.mail_address =  address.id if address else None

    @classmethod
    def by_name(cls, name):
        try:
            school = Session.query(cls).filter(cls.name==name).one()
        except orm.exc.NoResultFound:
            school = False
        return school

def create_school(name):
    school = School(name)
    Session.add(school)
    Session.commit()
    return school
