# encoding: utf-8
from . import *


def a(
        content="",
        href=False,
        tableIndex=False,
        thumbnail=False,
        pull=False,
        triggerStyle=False,
        htmlClass=False,
        htmlId=False,
        notification=False,
        postInBackground=False,
        openInNewTab=False,
        popover=False):
    """
    *Generate an anchor - TBS style*

    **Key Arguments:**
        - ``content`` -- the content
        - ``href`` -- the href link for the anchor
        - ``tableIndex`` -- table index for the dropdown menus [ False | -1 ]
        - ``pull`` -- direction to float the link (esp if image)
        - ``triggerStyle`` -- link to be used as a dropDown or tab trigger? [ False | "dropdown" | "tab" | "thumbnail" ]
        - ``htmlClass`` -- the class of the link
        - ``htmlId`` -- the html id of the anchor
        - ``postInBackground`` -- post to the href in the background, to fire data off to a cgi script to action without leaving page
        - ``notification`` -- a notification to be displayed on webpage
        - ``openInNewTab`` -- open the link in a new tab?

    **Return:**
        - ``a`` -- the a
    """
    triggerClass = ""
    dropdownCaret = ""

    falseList = [href, triggerClass,
                 triggerStyle, tableIndex, dropdownCaret, pull]
    for i in range(len(falseList)):
        if not falseList[i]:
            falseList[i] = ""
    [href, triggerClass, triggerStyle,
        tableIndex, dropdownCaret, pull] = falseList

    if popover is False:
        popover = ""

    if openInNewTab is not False:
        openInNewTab = """target="_blank" """
    else:
        openInNewTab = ""

    if not htmlId:
        htmlId = ""
    else:
        htmlId = 'id="%(htmlId)s"' % locals()

    if notification is False:
        notification = ""
    else:
        notification = """notification="%(notification)s" """ % locals()

    if tableIndex is True:
        tableIndex = """tableIndex = "%(tableIndex)s" """ % locals()

    if thumbnail:
        thumbnail = "thumbnail"
    else:
        thumbnail = ""

    if htmlClass is False:
        htmlClass = ""

    if pull:
        pull = "pull-%(pull)s" % locals()

    if postInBackground is True:
        postInBackground = "postInBackground"
    else:
        postInBackground = ""

    if triggerStyle == "dropdown":
        triggerClass = "dropdown-toggle"
        triggerToggle = """data-toggle="dropdown" """
        dropdownCaret = """<b class="caret"></b> """
    elif triggerStyle in ["tab", "modal"]:
        triggerToggle = """data-toggle="%(triggerStyle)s" """ % locals()
    else:
        triggerToggle = ""

    a = """<a %(tableIndex)s href="%(href)s" %(popover)s class="%(triggerClass)s %(thumbnail)s %(pull)s %(htmlClass)s %(postInBackground)s"  %(openInNewTab)s %(htmlId)s %(triggerToggle)s %(notification)s>%(content)s%(dropdownCaret)s</a>""" % locals()

    return a
