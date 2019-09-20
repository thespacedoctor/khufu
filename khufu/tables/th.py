# encoding: utf-8
from . import *


def th(
        content="",
        color=False,
        href=False,
        popover=False,
        span=False,
        columnWidth=False):
    """
    *Generate a table header cell - TBS style*

    **Key Arguments:**
        - ``content`` -- the content
        - ``color`` -- [ sucess | error | warning | info ]
        - ``href`` -- add a link for the header cell (to sort for example)
        - ``popover`` -- add helper text

    **Return:**
        - ``th`` -- the table header cell
    """
    if color is False:
        color = ""

    if href is False:
        href = ""
        link = ""
    else:
        href = """href="%(href)s" """ % locals()
        link = "link"

    if span is False:
        span = ""
    else:
        span = "span%(span)s" % locals()

    if columnWidth is False:
        columnWidth = ""
    else:
        columnWidth = """style="width: %(columnWidth)s%%;" """ % locals()

    if popover is False:
        popover = ""

    th = """<th %(href)s class="%(color)s %(link)s %(span)s" %(columnWidth)s %(popover)s>%(content)s</th>""" % locals()

    return th
