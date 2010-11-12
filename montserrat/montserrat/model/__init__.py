"""The application's model objects"""
from montserrat.model.meta import Session, Base

from montserrat.model.user import User
from montserrat.model.profile import Profile
from montserrat.model.media import Media
from montserrat.model.company import Company
from montserrat.model.school import School
from montserrat.model.address import Address

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)
