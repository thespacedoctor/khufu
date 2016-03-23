# encoding: utf-8
from . import *

# LAST MODIFIED : April 13, 2013
# CREATED : April 13, 2013
# AUTHOR : DRYX


def abbr(
        abbreviation="",
        fullWord=""):
    """
    *Get HTML5 Abbreviation*

    **Key Arguments:**
        - ``abbreviation`` -- the abbreviation
        - ``fullWord`` -- the full word

    **Return:**
        - abbr
    """

    abbr = """<abbr title="%(fullWord)s" class="initialism">%(abbreviation)s</abbr>""" % locals(
    )

    return abbr
