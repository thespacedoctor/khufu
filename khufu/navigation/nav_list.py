# encoding: utf-8
from . import *


def nav_list(
    itemList=[],
    pull=False,
    onPhone=True,
    onTablet=True,
    onDesktop=True,
):
    """ *Create an html list of navigation items from the required python list*

    **Key Arguments:**
        - ``itemList`` -- items to be included in the navigation list
        - ``pull`` -- float the nav-list [ False | 'right' | 'left' ]
        - ``onPhone`` -- does this container get displayed on a phone sized screen
        - ``onTablet`` -- does this container get displayed on a tablet sized screen
        - ``onDesktop`` -- does this container get displayed on a desktop sized screen

    **Return:**
        - navList """

    if pull:
        pull = """pull-%(pull)s""" % locals()
    else:
        pull = ''
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

    navList = """<ul class="nav %(pull)s %(onPhone)s %(onTablet)s %(onDesktop)s">""" % locals(
    )

    for item in itemList:
        navList = """%(navList)s
            <li>
                %(item)s
            </li>""" % locals()
    navList = """%(navList)s</ul>""" % locals()
    return navList
