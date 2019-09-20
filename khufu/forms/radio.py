# encoding: utf-8
from . import *


def radio(
        optionText="",
        optionNumber=1,
        htmlId=False,
        inlineHelpText=False,
        blockHelpText=False,
        disabled=False,
        checked=False):
    """
    *Generate a radio - TBS style*

    **Key Arguments:**
        - ``optionText`` -- the text associated with this checkbox
        - ``optionNumber`` -- the order in the option list
        - ``htmlId`` -- the html id of the element
        - ``inlineHelpText`` -- inline and block level support for help text that appears around form controls
        - ``blockHelpText`` -- a longer block of help text that breaks onto a new line and may extend beyond one line
        - ``disabled`` -- add the disabled attribute on an input to prevent user input
        - ``checked`` -- is the radio button checked by default

    **Return:**
        - ``radio`` -- the radio
    """
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

    if disabled:
        disabled = """disabled"""
        disabledId = "disabledId"
    else:
        disabled = ""
        disabledId = ""

    if checked is False:
        checked = ""
    else:
        checked = "checked"

    if not htmlId:
        htmlId = ""

    radio = """
        <label class="radio">
          <input type="radio" name="%(htmlId)s" id="%(htmlId)s %(disabledId)s %(htmlId)s" value="%(optionText)s" %(checked)s %(disabled)s>
            %(optionText)s
        </label>%(inlineHelpText)s%(inlineHelpText)s""" % locals()

    return radio
