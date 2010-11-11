# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1289519063.0448229
_template_filename=u'/home/maguire/microscholarships/montserrat/montserrat/templates/common/base.html'
_template_uri=u'/common/base.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['footer', 'header', 'flash', 'title']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">\n<html>\n  <head>\n    <title>Montserrat</title>\n    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">\n  </head>\n  <body>\n    <div id="header">\n      ')
        # SOURCE LINE 9
        __M_writer(escape(self.header()))
        __M_writer(u'\n    </div>\n\n    <div id="content">\n      <div class="inner">\n        <div class="msg">')
        # SOURCE LINE 14
        __M_writer(escape(self.flash()))
        __M_writer(u'</div>\n\n        ')
        # SOURCE LINE 16
        __M_writer(escape(next.body()))
        __M_writer(u'\n      </div>\n    </div>\n\n    <div id="footer">\n      ')
        # SOURCE LINE 21
        __M_writer(escape(self.footer()))
        __M_writer(u'\n    </div>\n  </body>\n</html>\n\n')
        # SOURCE LINE 26
        __M_writer(u'\n\n')
        # SOURCE LINE 28
        __M_writer(u'\n\n')
        # SOURCE LINE 30
        __M_writer(u'\n\n')
        # SOURCE LINE 32
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_flash(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


