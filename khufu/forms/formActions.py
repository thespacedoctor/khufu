# encoding: utf-8
from . import *


def formActions(
        primaryButton="",
        button2=False,
        button3=False,
        button4=False,
        button5=False,
        inlineHelpText=False,
        blockHelpText=False):
    """
    *Generate a formActions - TBS style*

    **Key Arguments:**
        - ``primaryButton`` -- the primary button
        - ``button2`` -- another button
        - ``button3`` -- another button
        - ``button4`` -- another button
        - ``button5`` -- another button
        - ``inlineHelpText`` -- inline and block level support for help text that appears around form controls
        - ``blockHelpText`` -- a longer block of help text that breaks onto a new line and may extend beyond one line

    **Return:**
        - ``formActions`` -- the formActions
    """
    falseList = [primaryButton, button2, button3,
                 button4, button5, inlineHelpText]

    for i in range(len(falseList)):
        if not falseList[i]:
            falseList[i] = ""

    [primaryButton, button2, button3, button4,
        button5, inlineHelpText] = falseList

    if inlineHelpText:
        inlineHelpText = """<span class="help-inline">%(inlineHelpText)s</span>""" % locals(
        )
    else:
        inlineHelpText = ""

    if blockHelpText:
        blockHelpText = """<span class="help-block">%(blockHelpText)s</span>""" % locals(
        )
    else:
        blockHelpText = ""

    formActions = """
        <div class="form-actions">
          %(primaryButton)s
          %(button2)s
          %(button3)s
          %(button4)s
          %(button5)s
        </div>%(inlineHelpText)s%(blockHelpText)s""" % locals()

    return formActions
