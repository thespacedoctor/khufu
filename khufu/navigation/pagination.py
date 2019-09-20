# encoding: utf-8
from . import *


def pagination(
        listItems="",
        size="default",
        align="left"):
    """
    *Generate pagination - TBS style. Simple pagination inspired by Rdio, great for apps and search results.*

    **Key Arguments:**
        - ``listItems`` -- the numbered items to be listed within the <ul> of the pagination block
        - ``size`` -- additional pagination block sizes [ "mini" | "small" | "default" | "large" ]
        - ``align`` -- change the alignment of pagination links [ "left" | "center" | "right" ]

    **Return:**
        - ``pagination`` -- the pagination
    """
    if size == "default":
        size = ""
    else:
        size = "pagination-%(size)s" % locals()
    if align == "left":
        align = ""
    else:
        align = "pagination-%(align)s" % locals()

    pagination = """
        <div class="pagination %(size)s %(align)s" id="  ">
            <ul>
            %(listItems)s
            </ul>
        </div>""" % locals()

    return pagination
