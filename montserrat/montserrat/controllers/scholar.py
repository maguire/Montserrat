import logging
import json

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from montserrat.lib.base import BaseController, render
from montserrat.model.user import User, ScholarUser, DonorUser
from montserrat.model.profile import Profile


log = logging.getLogger(__name__)

def check_loggedin(fn):
    if session.keys().count("user") > 0 \
        and not session["user"]["id"] == None \
        and User.by_id(session["user"]["id"]) :
            return fn
    else:
       abort(401, "Not Authorized")

class ScholarController(BaseController):
    
    def index(self):
        return render("scholar/index.html")
    
    @check_loggedin
    def profile_edit(self):
        user = ScholarUser.by_id(session["user"]["id"])
        profile = Profile.by_user_id(session["user"]["id"])
        if user:
            c.user = user
        if profile:
            c.profile = profile
        return render("/scholar/edit.html")

