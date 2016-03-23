# encoding: utf-8
from . import *

# LAST MODIFIED : April 16, 2013
# CREATED : April 16, 2013
# AUTHOR : DRYX


def thead(
        trContent=""):
    """
    *Generate a table head - TBS style*

    **Key Arguments:**
        - ``trContent`` -- the table row content

    **Return:**
        - ``thead`` -- the table head
    """
    thead = """<thead class="">%(trContent)s</thead>""" % locals()

    return thead
