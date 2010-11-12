# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1289537607.3853879
_template_filename='/home/maguire/microscholarships/montserrat/montserrat/templates/users/new.html'
_template_uri='users/new.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/common/base.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 3
        __M_writer(u'\n\n\n<form method="post" action="/users/create">\n  <div>\n    <div>User Type:</div>\n    <div><input type="radio" value="scholar" name="user_type" /> Scholar </div>\n    <div><input type="radio" value="donor"   name="user_type" /> Donor </div>\n  <div>\n  <div>\n    <div>First name:</div>\n    <div><input type="text" class="input" name="firstname" /></div>\n  </div>\n  <div>\n    <div>Last name:</div>\n    <div><input type="text" class="input" name="lastname" /></div>\n  </div>\n  <div>\n    <div>Username:</div>\n    <div><input type="text" class="input" name="username" /></div>\n  </div>\n  <div>\n    <div>E-mail:</div>\n    <div><input type="text" class="input" name="email" /></div>\n  </div>\n  <div>\n    <div>Password:</div>\n    <div><input type="password" class="input" name="password" /></div>\n  </div>\n    <div><input type="submit" value="Register" /> </div>\n  </div>\n</form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'Register')
        return ''
    finally:
        context.caller_stack._pop_frame()


