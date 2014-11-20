# encoding: utf-8
from . import *

# LAST MODIFIED : 20130508
# CREATED : 20130508
# AUTHOR : DRYX


def thumbnails(
        listItems=[]
):
    """Generate a thumbnail - TBS style

    **Key Arguments:**
        - ``htmlContent`` -- the html content of the thumbnail

    **Return:**
        - ``thumbnail`` -- the thumbnail with HTML content
    """
    theseItems = ""
    for item in listItems:
        theseItems = "%(theseItems)s %(item)s" % locals()

    thumbnails = """<ul class="thumbnails" id="  ">%(theseItems)s</ul>""" % locals(
    )

    return thumbnails
