# encoding: utf-8
from . import *


def ul(
        itemList=[],
        unstyled=False,
        inline=False,
        dropDownMenu=False,
        navStyle=False,
        navPull=False,
        navDirection="horizontal",
        breadcrumb=False,
        pager=False,
        thumbnails=False,
        mediaList=False,
        htmlId=False
):
    """
    *Get An unordered list -- can be used for navigation, stacked tab and pill*

    **Key Arguments:**
        - ``itemList`` -- a list of items to be included in the unordered list
        - ``unstyled`` -- is the list to be unstyled (first children only)
        - ``inline`` -- place all list items on a single line with inline-block and some light padding.
        - ``dropDownMenu`` -- is this ul to be used in a dropdown menu? [ false | true ]
        - ``navStyle`` -- set the navigation style if used for tabs & pills etc [ nav | tabs | pills | list ]
        - ``navPull`` -- set the alignment of the navigation links [ false | left | right ]
        - ``navDirection`` -- set the direction of the navigation [ 'default' | 'stacked' ]
        - ``breadcrumb`` -- display breadcrumb across muliple pages? [ False | True ]
        - ``pager`` -- use <ul> for a pager
        - ``thumbnails`` -- use the <ul> for a thumnail block?
        - ``mediaList`` -- use the <ul> for a media object list?
        - ``htmlId`` -- the html id of the ul

    **Return:**
        - ul
    """
    role = False
    falseList = [unstyled, inline, dropDownMenu, role, navStyle,
                 navPull, navDirection, breadcrumb, pager, thumbnails, mediaList]

    for i in range(len(falseList)):
        if not falseList[i]:
            falseList[i] = ""

    [unstyled, inline, dropDownMenu, role, navStyle, navPull,
        navDirection, breadcrumb, pager, thumbnails, mediaList] = falseList

    thisList = ""
    for i, item in enumerate(itemList):
        if "<li" in item:
            thisList = """%(thisList)s %(item)s""" % locals()
        else:
            thisList = """%(thisList)s <li>%(item)s</li>""" % locals()
        if i + 1 != len(itemList) and breadcrumb:
            thisList = thisList[:-5] + \
                """    <span class="divider">/</span></li>""" % locals()

    if unstyled:
        unstyled = "unstyled"

    if inline:
        inline = "inline"

    if dropDownMenu is True:
        dropDownMenu = "dropdown-menu"
        role = "menu"

    navStyleList = ["tabs", "pills", "list"]
    if navStyle:
        thisNavStyle = "nav"
    if navStyle in navStyleList:
        thisNavStyle = "%(thisNavStyle)s nav-%(navStyle)s" % locals()
    else:
        thisNavStyle = ""

    if navPull:
        navPull = "pull-%(navPull)s" % locals()

    if navDirection == "stacked":
        navDirection = "nav-stacked"
    elif navDirection == "horizontal":
        navDirection = ""
    else:
        navDirection = ""

    if breadcrumb is True:
        breadcrumb = "breadcrumb"

    if pager is True:
        pager = "pager"

    if thumbnails is True:
        thumbnails = "thumbnails"

    if mediaList is True:
        mediaList = "media-list"

    if not htmlId:
        htmlId = ""
    else:
        htmlId = 'id="%(htmlId)s"' % locals()

    ul = """<ul class="%(unstyled)s %(inline)s %(dropDownMenu)s %(role)s %(navPull)s %(thisNavStyle)s %(navDirection)s %(breadcrumb)s %(pager)s %(thumbnails)s %(mediaList)s" %(htmlId)s>%(thisList)s</ul>""" % locals(
    )

    return ul
