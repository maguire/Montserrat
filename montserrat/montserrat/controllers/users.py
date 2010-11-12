import logging
import hashlib
import json

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from montserrat.lib.base import BaseController, Session, render
from montserrat.model.user import User, ScholarUser, DonorUser

log = logging.getLogger(__name__)

class UsersController(BaseController):

    def new(self):
        return render("users/new.html")

    def create(self):
        user = self._find(username=request.params['username'])
        if user:
            # The client tried to create a user that already exists
            abort(409, '409 Conflict',
                  headers=[('location', url('user', id=user.username))])  

        user_dict = {}
        for param in request.params:
            if param == "user_type":
                 user_type = request.params[param]
            user_dict[param] = request.params[param]
        
        user_dict["password"] = hashlib.md5(request.params["password"]).hexdigest()
        
        if user_type == "scholar":
            new_user = ScholarUser(**user_dict)
        else :
            new_user = DonorUser(**user_dict)
        Session.add(new_user)
        Session.commit()
        return redirect("/")

    def login(self):
        return render("users/login.html")

    def dologin(self):
        if request.params["email"] and request.params["password"]:
            password = hashlib.md5(request.params["password"]).hexdigest()
            try:
                user = Session.query(User).filter(User.email==request.params["email"]).\
                    filter(User.password==password).one()
            except:
                return render("users/login.html")
            session["user"] = {"id": user.id, "name": "%s %s" % (user.firstname, user.lastname)}
            session.save()
            return redirect("/")
        else:
            return redirect("/users/login")

    def logout(self):
        if "user" not in session:
            return redirect("/")
        else:
            session.pop("user")
            session.save()
            return redirect("/")

    
    def _find(self, username):
        users = Session.query(User).filter(User.username.like(username+"%")).all()
        return users[0]

