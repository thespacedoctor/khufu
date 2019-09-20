# encoding: utf-8
from . import *


def label(text='', level='default'):
    """ *Generate a label - TBS style*

    **Key Arguments:**
        - ``text`` -- the text content
        - ``level`` -- the level colour of the label [ "default" | "success" | "warning" | "important" | "info" | "inverse" ]

    **Return:**
        - ``label`` -- the label """

    if level == 'default':
        level = ''
    else:
        level = 'label-%(level)s' % locals()
    label = """
        <span class="label %(level)s" id="  ">
            %(text)s
        </span>""" % locals()
    return label
