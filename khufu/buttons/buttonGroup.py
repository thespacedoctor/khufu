# encoding: utf-8
from . import *


def buttonGroup(
        buttonList=[],
        format="default",
        pull=False):
    """
    *Generate a buttonGroup - TBS style*

    **Key Arguments:**
        - ``buttonList`` -- a list of buttons
        - ``format`` -- format of the button [ default | toolbar | vertical ]

    **Return:**
        - ``buttonGroup`` -- the buttonGroup
    """
    thisButtonList = ""
    count = 1
    for button in buttonList:
        thisButtonList = "%(thisButtonList)s %(button)s" % locals()
        count += 1

    if pull is not False:
        pull = "pull-%(pull)s" % locals()
    else:
        pull = ""

    if format == "vertical":
        vertical = "btn-group-vertical"
    else:
        vertical = ""

    toolbar = ""
    if format == "toolbar":
        toolbar = "btn-toolbar"

    buttonGroup = """
        <div class="btn-group %(vertical)s %(toolbar)s %(pull)s"  id="  ">
            %(thisButtonList)s
        </div>""" % locals()

    return buttonGroup
