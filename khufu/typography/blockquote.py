# encoding: utf-8
from . import *

# LAST MODIFIED : April 13, 2013
# CREATED : April 13, 2013
# AUTHOR : DRYX


def blockquote(
        content="",
        source=False,
        pullRight=False):
    """
    *Get HTML5 Blockquote*

    **Key Arguments:**
        - ``content`` -- content to be quoted
        - ``source`` -- source of quote

    **Return:**
        - None
    """
    if source:
        source = """<small><cite title="%(source)s">%(source)s</cite></small>""" % locals(
        )
    else:
        source = ""

    if pullRight:
        pullRight = """class="pull-right" """
    else:
        pullRight = ""

    blockquote = """
        <blockquote %(pullRight)s>
            <p>%(content)s</p>
            %(source)s
        </blockquote>""" % locals()

    return blockquote
