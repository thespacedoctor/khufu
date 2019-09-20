# encoding: utf-8
from . import *


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
    html = html.replace("&lt;", "<")
    html = html.replace("&gt;", ">")
    html = html.replace("&quot;", '"')
    # THIS HAS TO BE LAST:
    html = html.replace("&amp;", "&")

    return html
