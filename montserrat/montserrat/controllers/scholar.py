import logging
import json

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from montserrat.lib.base import BaseController, Session, render
from montserrat.model.user import User, ScholarUser, DonorUser
from montserrat.model.profile import *
from montserrat.model.school import create_school


log = logging.getLogger(__name__)

#refactor out once it get used elsewhere (it will)
def check_loggedin(fn):
    if session.keys().count('user') > 0 \
        and not session['user']['id'] == None \
        and User.by_id(session['user']['id']) :
            return fn
    else:
       abort(401, "Not Authorized")

class ScholarController(BaseController):
       
    def index(self):
        return render("scholar/index.html")
    
    @check_loggedin
    def profile_edit(self):
        user = ScholarUser.by_id(session['user']['id'])
        profile = Profile.by_user_id(session['user']['id'])
        if user:
            c.user = user
        if profile:
            c.profile = profile
        return render("/scholar/edit.html")
    
    @check_loggedin
    def profile_update(self):
        user = ScholarUser.by_id(session['user']['id'])
        profile = Profile.by_user_id(session['user']['id'])
        
        if 'school' in request.params :
            school = School.by_name(request.params['school'])
            if not school:
                school = create_school(request.params['school'])
            profile.school = school
            profile.school_id = school.id
        if 'major' in request.params :
            profile.major = request.params['major']
        if 'gpa' in request.params : 
            profile.gpa = request.params['gpa']
        if 'hometown' in request.params :
            profile.hometown = request.params['hometown']
        #birthdate
        #race
        #religion
        #activities
        Session.add(profile)
        Session.commit()

        return "Profile updated."

    @check_loggedin
    def picture_update(self):
        pass #for now
    
    @check_loggedin
    def picture_edit(self):
        user = ScholarUser.by_id(session['user']['id'])
        profile = Profile.by_user_id(session['user']['id'])
        
        if user:
            c.user = user
        if profile :
           c.profile = profile
        return render("/scholar/edit_picture.html")
