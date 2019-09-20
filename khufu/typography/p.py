# encoding: utf-8E
from . import *


def p(
        content="",
        lead=False,
        textAlign=False,
        color=False,
        navBar=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True,
        htmlId=False,
        htmlClass=False):
    """
    *Get a Paragraph element*

    **Key Arguments:**
        - ``content`` -- content of the paragraph
        - ``lead`` -- is this a lead paragraph?
        - ``textAlign`` -- how to align paragraph text [ left | center | right ]
        - ``color`` -- colored text for emphasis [ muted | warning | info | error | success ]
        - ``navBar`` -- is this <p> for a navbar?
        - ``onPhone`` -- does this container get displayed on a phone sized screen
        - ``onTablet`` -- does this container get displayed on a tablet sized screen
        - ``onDesktop`` -- does this container get displayed on a desktop sized screen

    **Return:**
        - ``p`` -- the html paragraph element
    """
    falseList = [lead, textAlign, ]
    for i in range(len(falseList)):
        if not falseList[i]:
            falseList[i] = ""
    [lead, textAlign, ] = falseList

    if htmlId is not False:
        htmlId = """id="%(htmlId)s" """ % locals()
    else:
        htmlId = ""

    if htmlClass is False:
        htmlClass = ""

    if textAlign:
        textAlign = "text-%(textAlign)s" % locals()
    else:
        textAlign = ""

    if lead is True:
        lead = "lead"

    if color is False:
        color = ""
    elif color == "muted":
        color = "muted"
    else:
        color = """text-%(color)s""" % locals()

    if navBar is True:
        navBar = "navbar-text"
    else:
        navBar = ""

    if onPhone:
        onPhone = ""
    else:
        onPhone = "hidden-phone"
    if onTablet:
        onTablet = ""
    else:
        onTablet = "hidden-tablet"
    if onDesktop:
        onDesktop = ""
    else:
        onDesktop = "hidden-desktop"

    p = """
        <p class="%(lead)s %(onPhone)s %(onTablet)s %(onDesktop)s %(textAlign)s %(color)s %(navBar)s %(htmlClass)s" %(htmlId)s>%(content)s</p>
    """ % locals()

    return p
