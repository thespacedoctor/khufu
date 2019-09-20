# encoding: utf-8
from . import *


def navBar(
    brand='',
    contentList=[],
    contentListPull=False,
    dividers=False,
    forms=False,
    fixedOrStatic=False,
    location='top',
    responsive=False,
    dark=False,
    transparent=False,
    htmlClass=False
):
    """ *Generate a navBar - TBS style*

    **Key Arguments:**
        - ``brand`` -- the website brand [ image | text ]
        - ``contentList`` -- the content list of li and dropdowns
        - ``contentListPull`` -- False, right, left
        - ``fixedOrStatic`` -- Fix the navbar to the top or bottom of the viewport, or create a static full-width navbar that scrolls away with the page [ False | fixed | static ]
        - ``location`` -- location of the navigation bar if fixed or static
        - ``dark`` -- Modify the look of the navbar by making it dark
        - ``transparent`` -- make the bar see-through

    **Return:**
        - ``navBar`` -- the navBar """

    if brand is not False:
        brand = u"""<a class="brand" href="#">%(brand)s</a>""" % locals()
    else:
        brand = u""
    toggleButton = ""
    falseList = [dividers, fixedOrStatic, toggleButton, dark]
    for i in range(len(falseList)):
        if not falseList[i]:
            falseList[i] = ""
    [dividers, fixedOrStatic, toggleButton, dark] = falseList
    if dividers:
        dividers = u"""<li class="divider-vertical"></li>"""
    titleList = ''
    # contentList = ''
    count = 0

    if htmlClass is False:
        htmlClass = ""

    if contentListPull is not False:
        contentListPull = u"pull-%(contentListPull)s" % locals()

    for item in contentList:
        item = u"""<li>%(item)s</li>""" % locals()
        titleList = u"""%(titleList)s %(item)s %(dividers)s""" % locals()

    titleList = u"""
    <ul class="nav %(contentListPull)s" id="  ">
        %(titleList)s
    </ul>
    """ % locals()

    formList = ""
    if forms:
        formList = forms

    if fixedOrStatic:
        fixedOrStatic = u'navbar-%(fixedOrStatic)s-%(location)s' % locals()
    if responsive:
        toggleButton = \
            u"""
            <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
              </a>
        """
        titleList = u"""
            <div class="nav-collapse collapse">
                %(titleList)s
            </div>""" \
            % locals()
    if dark is True:
        dark = "navbar-inverse"
    else:
        dark = ""

    if transparent is True:
        transparent = u"navbar-transparent"
    else:
        transparent = ""

    navBar = \
        u"""
        <div class="navbar %(fixedOrStatic)s %(dark)s %(transparent)s %(htmlClass)s">
          <div class="navbar-inner">
            %(brand)s
            %(titleList)s
            %(formList)s
          </div>
        </div>
        """ % locals()
    return navBar
