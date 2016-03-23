# encoding: utf-8
from . import *

# LAST MODIFIED : May 28, 2013
# CREATED : May 28, 2013
# AUTHOR : DRYX


def unescape_html(html):
    """
    *Unescape a string previously escaped with cgi.escape()*

    **Key Arguments:**
        - ``dbConn`` -- mysql database connection
        - ``log`` -- logger
        - ``html`` -- the string to be unescaped

    **Return:**
        - ``html`` -- the unescaped string
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    ################ > VARIABLE SETTINGS ######

    ################ >ACTION(S) ################
    html = html.replace("&lt;", "<")
    html = html.replace("&gt;", ">")
    html = html.replace("&quot;", '"')
    # this has to be last:
    html = html.replace("&amp;", "&")

    return html
