# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1289600460.910125
_template_filename='/home/maguire/microscholarships/montserrat/montserrat/templates/scholar/edit.html'
_template_uri='/scholar/edit.html'
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
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 4
        __M_writer(u'\n\n<div>\n    <form action="/scholar/profile_save" method="post">\n        <div>First Name</div>\n        <div>\n            <input name="firstname" value="')
        # SOURCE LINE 10
        __M_writer(escape(c.user.firstname))
        __M_writer(u'" />\n        </div>\n        <div>Last Name</div>\n        <div>\n            <input name="lastname" value="')
        # SOURCE LINE 14
        __M_writer(escape(c.user.lastname))
        __M_writer(u'" />\n        </div>\n        <div>Profile Picture</div>\n        <div>\n           <input />\n        </div>\n        <div>School</div>\n        <div>\n            <input name="school" value="')
        # SOURCE LINE 22
        __M_writer(escape(c.profile.school_id))
        __M_writer(u'" />\n        </div>\n    </form>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'Scholar Profile Edit')
        return ''
    finally:
        context.caller_stack._pop_frame()


