import logging
import hashlib
import json

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from montserrat.lib.base import BaseController, Session, render
from montserrat.model.user import User, ScholarUser, DonorUser
from montserrat.model.profile import Profile

log = logging.getLogger(__name__)

class ScholarController(BaseController):
    
    def index(self):
        return render("scholar/index.html")

    def profile_edit(self):
        if session.keys().count("user") > 0 and session["user"] :
            try :
                user = Session.query(ScholarUser).filter(ScholarUser.id==session["user"]["id"]).one()
                profile = Session.query(Profile).filter(Profile.user_id==user.id).one()
            except :
                abort(401, '401: Permission Denied')
            
            c.user = user
            c.profile = profile
            return render("/scholar/edit.html")
        else :
            return redirect("/users/login")

