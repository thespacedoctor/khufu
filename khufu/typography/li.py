# encoding: utf-8
from . import *


def li(
        content="",
        span=False,
        disabled=False,
        submenuTitle=False,
        divider=False,
        navStyle=False,
        navDropDown=False,
        pager=False,
        pull=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True,
        indent=False,
        hidden=False):
    """
    *Generate a li - TBS style*

    **Key Arguments:**
        - ``content`` -- the content (if a subMenu for dropdown this should be <ul>)
        - ``span`` -- the column span [ False | 1-12 ]
        - ``disabled`` -- add the disabled attribute on an grey out this list item. Note you can optionally swap anchors for spans to remove click functionality.
        - ``submenuTitle`` -- if a submenu (<ul>) is to be included as content, use this as the title.
        - ``divider`` -- if true this list item shall be a line
        - ``navStyle`` -- how is the navigation element to be displayed? [ active | header ]
        - ``navDropDown`` -- true if the list item is to be used as a dropdown in navigation
        - ``pager`` -- use the <li> within a pager navigation? [ False | "previous" | "next" ]

    **Return:**
        - ``li`` -- the li
    """
    submenuClass = False
    falseList = [disabled, submenuClass,
                 submenuTitle, navStyle, navDropDown, pager, span]
    for i in range(len(falseList)):
        if not falseList[i]:
            falseList[i] = ""
    [disabled, submenuClass, submenuTitle,
        navStyle, navDropDown, pager, span] = falseList

    if pull:
        pull = "pull-%(pull)s" % locals()
    else:
        pull = ""

    if disabled:
        disabled = """disabled"""

    if submenuTitle:
        submenuClass = "dropdown-submenu"
        submenuTitle = """<a tabindex="-1" href="#">%(submenuTitle)s</a>""" % locals(
        )

    if navStyle == "active":
        if "href" in content:
            content = content.replace('class="', 'class="active ')
    elif navStyle:
        navStyle = "nav-%(navStyle)s" % locals()

    if navDropDown:
        navDropDown = """dropdown"""

    if span:
        span = "span%(span)s" % locals()

    if indent:
        indent = """style="padding-left: 1em" """
    else:
        indent = ""

    if hidden:
        hidden = "hidden"
    else:
        hidden = ""

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

    li = """<li class="%(disabled)s %(phoneClass)s %(tabletClass)s %(desktopClass)s %(submenuClass)s %(navStyle)s %(pager)s %(span)s %(navDropDown)s %(pull)s %(hidden)s" %(indent)s id="  ">%(submenuTitle)s%(content)s</li>""" % locals(
    )

    if divider is True:
        li = """<li class="divider"></li>"""

    return li
