# encoding: utf-8
from . import *


def pageHeader(
        headline="",
        tagline=""):
    """
    *Generate a pageHeader - TBS style*

    **Key Arguments:**
        - ``headline`` -- the headline text
        - ``tagline`` -- the tagline text for below the headline

    **Return:**
        - ``pageHeader`` -- the pageHeader
    """
    pageHeader = """
        <div class="page-header" id="  ">
            <h1>%(headline)s<br><small>%(tagline)s</small></h1>
        </div>""" % locals()

    return pageHeader
