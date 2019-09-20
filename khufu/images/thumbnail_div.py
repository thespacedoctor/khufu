# encoding: utf-8
from . import *


def thumbnail_div(
        div_content=""
):
    """
    *Generate a thumbnail - TBS style*

    **Key Arguments:**
        - ``div_content`` -- the html content of the thumbnail

    **Return:**
        - ``thumbnail`` -- the thumbnail with HTML content
    """
    thumbnail_div = """<div class="thumbnail" id="  ">%(div_content)s</div>""" % locals(
    )

    return thumbnail_div
