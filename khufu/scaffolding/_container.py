# encoding: utf-8
from . import *


def _container(
    responsive=True,
    content='',
    htmlId=False,
    htmlClass=False,
    onPhone=True,
    onTablet=True,
    onDesktop=True,
):
    """ *The over-all content container for the twitter bootstrap webpage*

    **Key Arguments:**
        - ``responsive`` -- fluid layout if true, fixed if false
        - ``content`` -- html content of the container div
        - ``htmlId`` -- the id of the container
        - ``htmlClass`` -- the class of the container
        - ``onPhone`` -- does this container get displayed on a phone sized screen
        - ``onTablet`` -- does this container get displayed on a tablet sized screen
        - ``onDesktop`` -- does this container get displayed on a desktop sized screen

    **Return:**
        - ``container`` 
    """

    if responsive:
        responsive = '-fluid'
    else:
        responsive = ''
    if htmlId:
        htmlId = """id="%(htmlId)s" """ % locals()
    else:
        htmlId = ''
    if not htmlClass:
        htmlClass = ''
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
    container = """
        <div class="container%(responsive)s %(htmlClass)s %(onPhone)s %(onTablet)s %(onDesktop)s" %(htmlId)s>
            %(content)s
        </div>
    """ % locals()
    return container
