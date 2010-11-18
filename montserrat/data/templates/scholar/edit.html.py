# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1290108467.863148
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
        __M_writer(u'\n\n<div>\n    <form action="/scholar/profile_update" method="post">\n        <div>First Name</div>\n        <div>\n            ')
        # SOURCE LINE 10
        __M_writer(escape(c.user.firstname))
        __M_writer(u'\n        </div>\n        <div>Last Name</div>\n        <div>\n            ')
        # SOURCE LINE 14
        __M_writer(escape(c.user.lastname))
        __M_writer(u'\n        </div>\n        <div>Hometown</div>\n        <div>\n           <input name="hometown" value="')
        # SOURCE LINE 18
        __M_writer(escape(c.profile.hometown))
        __M_writer(u'" />\n        </div>\n        <div>School</div>\n        <div>\n')
        # SOURCE LINE 22
        if c.profile.school :
            # SOURCE LINE 23
            __M_writer(u'                <input name="school" value="')
            __M_writer(escape(c.profile.school.name))
            __M_writer(u'" />\n')
            # SOURCE LINE 24
        else :
            # SOURCE LINE 25
            __M_writer(u'                <input name="school" />\n')
            pass
        # SOURCE LINE 27
        __M_writer(u'        </div>\n        <div>Major</div>\n        <div>\n            <input name="major" value="')
        # SOURCE LINE 30
        __M_writer(escape(c.profile.major))
        __M_writer(u'" />\n        </div>\n        <div>GPA</div>\n        <div>\n            <input name="gpa" value="')
        # SOURCE LINE 34
        __M_writer(escape(c.profile.gpa))
        __M_writer(u'" />\n        </div>\n        <div>\n            <input type="submit" name="submit" value="submit" />\n        </div>\n    </form>\n</div>\n')
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


