# encoding: utf-8
from . import *


def address(
        name=False,
        addressLine1=False,
        addressLine2=False,
        addressLine3=False,
        phone=False,
        email=False,
        twitterHandle=False):
    """
    *Get The HTML5 address element*

    **Key Arguments:**
        - ``name`` -- name of person
        - ``addressLine1`` -- first line of the address
        - ``addressLine2`` -- second line of the address
        - ``addressLine3`` -- third line of the address
        - ``phone`` -- telephone number
        - ``email`` -- email address
        - ``twitterHandle`` -- twitter handle

    **Return:**
        - address
    """

    falseList = [name, addressLine1, addressLine2,
                 addressLine3, phone, email, twitterHandle]
    for item in falseList:
        if not item:
            item = ""

    if name:
        name = "<strong>%(name)s</strong><br>" % locals()
    else:
        name = ""

    if addressLine1:
        addressLine1 = "%(addressLine1)s<br>" % locals()
    else:
        addressLine1 = ""
    if addressLine2:
        addressLine2 = "%(addressLine2)s<br>" % locals()
    else:
        addressLine2 = ""
    if addressLine3:
        addressLine3 = "%(addressLine3)s<br>" % locals()
    else:
        addressLine3 = ""
    if phone:
        phone = """<abbr title="Phone">p:</abbr> %(phone)s<br>""" % locals()
    else:
        phone = ""
    if email:
        email = """<abbr title="email">e:</abbr> <a href="mailto:#">%(email)s</a><br>""" % locals(
        )
    else:
        email = ""
    if twitterHandle:
        twitterHandle = """<abbr title="twitter handle">t:</abbr> %(twitterHandle)s<br>""" % locals(
        )
    else:
        twitterHandle = ""

    address = """
        <address>
            %(name)s
            %(addressLine1)s
            %(addressLine2)s
            %(addressLine3)s
            %(phone)s
            %(email)s
            %(twitterHandle)s
        </address>
    """ % locals()

    return address
