# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="maguire"

from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, Unicode
from montserrat.model.meta import Base

class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True)
    street_address1 = Column(Unicode(100))
    street_address2 = Column(Unicode(100))
    city = Column(Unicode(100))
    state = Column(Unicode(100))
    country = Column(Unicode(100))
    zip_code = Column(Integer)

    def __init__(self, street_address1, city, state,zip_code, street_address2="",country="USA"):
        self.street_address1 = street_address1
        self.street_address2 = street_address2
        self.city = city
        self.state = state
        self.country = country
        self.zip_code = zip_code

