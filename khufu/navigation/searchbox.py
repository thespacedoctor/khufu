# encoding: utf-8
from . import *


def searchbox(
    size='medium',
    htmlId="",
    placeHolder=False,
    button=False,
    buttonSize='small',
    buttonColor='grey',
    navBar=False,
    pull=False,
    actionScript="#"
):
    """ *Create a Search box*

    **Key Arguments:**
        - ``size`` -- size = mini | small | medium | large | xlarge | xxlarge
        - ``htmlId`` -- the html id of the search bar
        - ``placeholder`` -- placeholder text
        - ``button`` -- do you want a search button?
        - ``buttonSize``
        - ``buttonColor``
        - ``actionScript`` -- the script used to action the search text

    **Return:**
        - ``markup`` -- markup for the searchbar """

    if button:
        button = """<button type="submit" class="btn-%(buttonSize)s btn-%(buttonColor)s">Search</button>""" % locals(
        )
    else:
        button = ''
    if placeHolder:
        placeHolder = """placeholder="%(placeHolder)s" """ % locals()
    else:
        placeHolder = ''
    if navBar:
        navBar = 'navbar-search'
    else:
        navBar = ''
    if pull:
        pull = """pull-%(pull)s""" % locals()
    else:
        pull = ''

    markup = \
        """
    <form class="form-search pull-right" action="%(actionScript)s">
      <input id="%(htmlId)s" name="%(htmlId)s" type="text" class="input-%(size)s search-query %(navBar)s %(pull)s" %(placeHolder)s >
      %(button)s
    </form>
    """ % locals()
    return markup
