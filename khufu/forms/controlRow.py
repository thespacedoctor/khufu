# encoding: utf-8
from . import *


def controlRow(inputList=[]):
    """
    *generate a form row*

    **Key Arguments:**
        - ``inputList`` -- list of inputs for the control row

    **Return:**
        - ``controlRow`` -- the controlRow
    """
    if len(inputList) > 1:
        row = "controls-row"
    else:
        row = ""

    content = ""
    for iinput in inputList:
        content = """%(content)s %(iinput)s""" % locals()

    controlRow = """
        <div class="controls %(row)s">
            %(content)s
        </div>""" % locals()

    return controlRow
