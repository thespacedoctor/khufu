# encoding: utf-8
from . import *


def td(
        content=False,
        color=False,
        span=False):
    """
    *Generate a table data cell - TBS style*

    **Key Arguments:**
        - ``content`` -- the content
        - ``color`` -- [ sucess | error | warning | info ]

    **Return:**
        - ``td`` -- the table data cell
    """
    if color is False:
        color = ""
    if content is False:
        content = ""
    if span is False:
        span = ""
    else:
        span = "span%(span)s" % locals()

    td = """<td class="%(color)s %(span)s">%(content)s</td>""" % locals()

    return td
