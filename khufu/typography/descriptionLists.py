# encoding: utf-8
from . import *

# LAST MODIFIED : April 13, 2013
# CREATED : April 13, 2013
# AUTHOR : DRYX


def descriptionLists(
        orderedDictionary={},
        sideBySide=False):
    """A list of definitions.

    **Key Arguments:**
        - ``orderedDictionary`` -- the ordered dictionary of the terms and their definitions
        - ``sideBySide`` -- Make terms and descriptions in <dl> line up side-by-side.

    **Return:**
        - None
    """

    termList = ""
    for k, v in orderedDictionary.iteritems():
        termList = """%(termList)s
            <dt>%(k)s</dt>
            <dd>%(v)s</dd>
        """ % locals()

    if sideBySide:
        sideBySide = "dl-horizontal"
    else:
        sideBySide = ""

    descriptionLists = """
        <dl class="%(sideBySide)s">
            %(termList)s
        </dl>
    """ % locals()

    return descriptionLists

