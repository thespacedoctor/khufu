# encoding: utf-8
from . import *

# LAST MODIFIED : April 16, 2013
# CREATED : April 16, 2013
# AUTHOR : DRYX


def tableCaption(
        content=""):
    """Generate a table caption - TBS style

    **Key Arguments:**
        - ``content`` -- the content

    **Return:**
        - ``tableCaption`` -- the table caption
    """
    tableCaption = """<caption class="">%(content)s</caption>""" % locals()

    return tableCaption
