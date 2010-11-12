# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="maguire"

from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, Unicode
from montserrat.model.meta import Base

class School(Base):
    __tablename__ = "school"

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(100))
    mail_address = Column(Integer, ForeignKey('address.id'))

    def __init__(self, name, address):
        self.name = name
        self.mail_address = address.id
