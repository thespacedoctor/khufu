# encoding: utf-8
from . import *

# LAST MODIFIED : July 22, 2013
# CREATED : July 22, 2013
# AUTHOR : DRYX


def is_navStyle_active(
        log,
        thisPageName,
        thisPageId):
    """
    *is navStyle active*

    **Key Arguments:**
        - ``log`` -- logger
        - ``thisPageName`` -- the thisPageName of the page
        - ``thisPageId`` -- the Id of this page

    **Return:**
        - ``navStyle`` -- boolean, true if the navStyle should be active, i.e. the link is to the currently viewed page

    .. todo::

    - [ ] when complete, clean is_navStyle_active function & add logging
    """
    ################ > IMPORTS ################
    ## STANDARD LIB ##
    ## THIRD PARTY ##
    ## LOCAL APPLICATION ##

    log.debug('starting the ``is_navStyle_active`` function')
    ## VARIABLES ##

    if thisPageName == thisPageId:
        navStyle = "active"
    else:
        navStyle = False

    log.debug('completed the ``is_navStyle_active`` function')
    return navStyle
