import logging
import json

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from montserrat.lib.base import BaseController, Session, render
from montserrat.model.user import *
from montserrat.model.profile import Profile

log = logging.getLogger(__name__)

class UsersController(BaseController):
    
    def index(self):
        return redirect("/users/login")

    def new(self):
        return render("users/new.mako")

    def create(self):
        user = User.by_name(username=request.params['username'])
        if user:
            # The client tried to create a user that already exists
            abort(409, '409 Conflict',
                  headers=[('location', url('user', id=user.username))])  

        user_dict = {}
        for param in request.params:
            if param == "user_type":
                 user_type = request.params[param]
            else :
                user_dict[param] = request.params[param]
        
        new_user = create_user(user_type, user_dict)
        
        #new_user does not have a user id until after commit
        if user_type == "scholar":
            Session.add(Profile(new_user))
            Session.commit()
          
        session["user"] = {"id": new_user.id, "name": "%s %s" % (new_user.firstname, new_user.lastname)}
        session.save()
        return redirect("/"+user_type+"/")

    def login(self):
        return render("users/login.mako")

    def dologin(self):
        if request.params["email"] and request.params["password"]:
            user = valid_login(request.params["email"], request.params["password"])
            if not user : return render("users/login.mako")
            session["user"] = {"id": user.id, "name": "%s %s" % (user.firstname, user.lastname)}
            session.save()
            return redirect("/"+user.user_type+"/")
        else:
            return redirect("/users/login")

    def logout(self):
        if "user" not in session:
            return redirect("/")
        else:
            session.pop("user")
            session.save()
            return redirect("/")

    
