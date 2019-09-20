# encoding: utf-8
from . import *


def tr(
        cellContent="",
        color=False,
        href=False,
        popover=False,
        span=False):
    """
    *Generate a table row - TBS style*

    **Key Arguments:**
        - ``cellContent`` -- the content - either <td>s or <th>s
        - ``color`` -- [ sucess | error | warning | info ]
        - ``href`` -- add a link for the whole table row

    **Return:**
        - ``tr`` -- the table row
    """

    if isinstance(cellContent, list):
        new = ""
        for c in cellContent:
            new += c
        cellContent = new

    if color is False:
        color = ""

    if href is False:
        href = ""
        link = ""
    else:
        href = """href="%(href)s" """ % locals()
        link = "link"

    if popover is False:
        popover = ""

    if span is False:
        span = ""
    else:
        span = "span%(span)s" % locals()

    tr = """<tr %(href)s class="%(link)s %(color)s %(span)s" %(popover)s>%(cellContent)s</tr>""" % locals()

    return tr
