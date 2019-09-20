# encoding: utf-8
from . import *


def horizontalFormControlGroup(
        content="",
        validationLevel=False,
        hidden=False):
    """
    *Generate a horizontal form control group (row) - TBS style*

    **Key Arguments:**
        - ``content`` -- the content
        - ``validationLevel`` -- validation level [ warning | error | info | success ]
        - ``hidden`` -- hide the CG from the user?

    **Return:**
        - ``horizontalFormControlGroup`` -- the horizontal form control group
    """
    falseList = [validationLevel, ]

    for i in range(len(falseList)):
        if not falseList[i]:
            falseList[i] = ""

    [validationLevel, ] = falseList

    if hidden:
        hidden = """hidden"""
    else:
        hidden = ""

    horizontalFormControlGroup = """
        <div class="control-group %(validationLevel)s %(hidden)s">
            %(content)s
        </div>""" % locals()

    return horizontalFormControlGroup
