# encoding: utf-8
from . import *


def ol(itemList=[]):
    """
    *An ordered list*

    **Key Arguments:**
        - ``itemList`` -- a list of items to be included in the ordered list

    **Return:**
        - ol
    """
    thisList = ""
    for item in itemList:
        if "<li" in item[:5]:
            thisList = """%(thisList)s\n%(item)s""" % locals()
        else:
            thisList = """%(thisList)s <li>%(item)s</li>\n""" % locals()

    ol = """
        <ol>
            %(thisList)s
        </ol>
    """ % locals()

    return ol
