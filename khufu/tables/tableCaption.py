# encoding: utf-8
from . import *


def tableCaption(
        content=""):
    """
    *Generate a table caption - TBS style*

    **Key Arguments:**
        - ``content`` -- the content

    **Return:**
        - ``tableCaption`` -- the table caption
    """
    tableCaption = """<caption class="">%(content)s</caption>""" % locals()

    return tableCaption
