# encoding: utf-8
from . import *


def badge(text='', level='default'):
    """ *Generate a badge - TBS style*

    **Key Arguments:**
        - ``text`` -- the text content
        - ``level`` -- the level colour of the badge [ "default" | "success" | "warning" | "important" | "info" | "inverse" ]

    **Return:**
        - ``badge`` -- the badge """

    if level == 'default':
        level = ''
    else:
        level = 'badge-%(level)s' % locals()
    badge = """
        <span class="badge %(level)s" id="  ">
            %(text)s
        </span>""" % locals()
    return badge
