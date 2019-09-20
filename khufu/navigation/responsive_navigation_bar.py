# encoding: utf-8
from . import *


def responsive_navigation_bar(
    shade='dark',
    brand=False,
    brandLink="#",
    loginDetails=False,
    outsideNavList=False,
    insideNavList=False,
    htmlId=False,
    onPhone=True,
    onTablet=True,
    onDesktop=True,
):
    """ *Create a twitter bootstrap responsive nav-bar component*

    **Key Arguments:**
        - ``shade`` -- if dark then colors are inverted [ False | 'dark' ]
        - ``brand`` -- the website brand [ image | text ]
        - ``outsideNavList`` -- nav-list to be contained outside collapsible content
        - ``insideNavList`` -- nav-list to be contained inside collapsible content
        - ``htmlId`` --
        - ``onPhone`` -- does this container get displayed on a phone sized screen
        - ``onTablet`` -- does this container get displayed on a tablet sized screen
        - ``onDesktop`` -- does this container get displayed on a desktop sized screen

    **Return:**
        - ``navBar`` -- """

    if not shade:
        shade = ''
    else:
        shade = 'navbar-inverse'
    if not brand:
        brand = ''
    else:
        brand = """<a  href="%(brandLink)s">%(brand)s</a>""" % locals(
        )

    if loginDetails:
        loginDetails = """<span class="login">%(loginDetails)s</span>""" % locals(
        )
        brand = "%(brand)s %(loginDetails)s " % locals(
        )
    brand = """<div class="brand">%(brand)s</a></div>""" % locals()

    if not outsideNavList:
        outsideNavList = ''

    thisList = ""
    if insideNavList:
        insideNavList = """<div class="nav-collapse collapse"><ul class="nav pull-right">%(insideNavList)s</ul></div>""" % locals(
        )
    else:
        insideNavList = ''

    if htmlId:
        htmlId = """id="%(htmlId)s" """ % locals()
    else:
        htmlId = ''
    if onPhone:
        onPhone = ''
    else:
        onPhone = 'hidden-phone'
    if onTablet:
        onTablet = ''
    else:
        onTablet = 'hidden-tablet'
    if onDesktop:
        onDesktop = ''
    else:
        onDesktop = 'hidden-desktop'
    navBar = """<div class="navbar %(shade)s %(onPhone)s %(onTablet)s %(onDesktop)s" %(htmlId)s>
    <div class="navbar-inner">
        <div class="container">
            <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </a>
            %(brand)s%(outsideNavList)s%(insideNavList)s
        </div>
    </div>
 </div>""" % locals()
    return navBar
