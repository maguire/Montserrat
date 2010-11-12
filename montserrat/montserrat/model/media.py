
# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="maguire"

from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, Unicode
from montserrat.model.meta import Base

class Media(Base):
    __tablename__ = "media"

    id = Column(Integer, primary_key=True)
    fs_location = Column(Unicode(200))
    web_location = Column(Unicode(200))
    filename = Column(Unicode(100))   
 
    def __init__(self, filename, fs_location, web_location):
        self.filename = filename
        self.fs_location = fs_location
        self.web_location = web_location
