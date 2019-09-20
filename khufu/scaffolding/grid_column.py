# encoding: utf-8
from . import *


def grid_column(
    span=1,
    offset=0,
    content='',
    htmlId=False,
    htmlClass=False,
    pull=False,
    onPhone=True,
    onTablet=True,
    onDesktop=True,
    dataspy=False
):
    """ *Get a column block for the Twiiter Bootstrap static layout grid.*

    **Key Arguments:**
        - ``log`` -- logger
        - ``span`` -- the relative width of the column
        - ``offset`` -- increase the left margin of the column by this amount
        - ``htmlId`` -- the id of the column
        - ``htmlClass`` -- the class of the column
        - ``pull`` -- left, right, or center
        - ``onPhone`` -- does this column get displayed on a phone sized screen
        - ``onTablet`` -- does this column get displayed on a tablet sized screen
        - ``onDesktop`` -- does this column get displayed on a desktop sized screen

    **Return:**
        - ``column`` -- the column """

    if htmlId:
        htmlId = """id="%(htmlId)s" """ % locals()
    else:
        htmlId = ''
    if not htmlClass:
        htmlClass = ''

    phoneClass = ""
    tabletClass = ""
    desktopClass = ""
    if onPhone:
        if onTablet:
            if not onDesktop:
                desktopClass = "hidden-desktop"
        else:
            if not onDesktop:
                phoneClass = "visible-phone"
            else:
                tabletClass = "hidden-tablet"
    else:
        if onTablet:
            if not onDesktop:
                tabletClass = "visible-tablet"
            else:
                phoneClass = "hidden-phone"
        else:
            desktopClass = "visible-desktop"

    if pull:
        pull = "pull-%(pull)s" % locals()
    else:
        pull = ""

    if dataspy is not False:
        dataspy = """data-spy="affix" data-offset-top="200" """
    else:
        dataspy = ""

    column = """
        <div %(dataspy)s class="span%(span)s offset%(offset)s %(htmlClass)s %(phoneClass)s %(tabletClass)s %(desktopClass)s %(pull)s" %(htmlId)s>
            %(content)s
        </div>
    """ % locals()
    return column
