# encoding: utf-8
from . import *


def grid_row(
    responsive=True,
    columns='',
    htmlId=False,
    htmlClass=False,
    onPhone=True,
    onTablet=True,
    onDesktop=True,
):
    """ *Create a row using the Twitter Bootstrap static layout grid.
    The static Bootstrap grid system utilizes 12 columns.*

    **Key Arguments:**
        - ``responsive`` -- fluid layout if true, fixed if false
        - ``columns`` -- coulmns to be included in this row
        - ``htmlId`` -- the id of the row
        - ``htmlClass`` -- the class of the row
        - ``onPhone`` -- does this row get displayed on a phone sized screen
        - ``onTablet`` -- does this row get displayed on a tablet sized screen
        - ``onDesktop`` -- does this row get displayed on a desktop sized screen

    **Return:**
        - ``row`` -- the row """

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
    row = """
        <div class="row%(responsive)s %(htmlClass)s %(onPhone)s %(onTablet)s %(onDesktop)s" %(htmlId)s>
            %(columns)s
        </div>
    """ % locals()
    return row
