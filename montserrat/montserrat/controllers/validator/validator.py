
from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect


def check_loggedin(fn):
    if session.keys.count("user") > 0
        and User.by_id(session["user"]["id"]) :
            return fn
    else:
        return redirect("/users/login")
