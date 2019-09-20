# encoding: utf-8
from . import *


def checkbox(
        optionText="",
        inline=False,
        optionNumber=1,
        htmlId=False,
        inlineHelpText=False,
        blockHelpText=False,
        disabled=False,
        checked=False):
    """
    *Generate a checkbox - TBS style*

    **Key Arguments:**
        - ``optionText`` -- the text associated with this checkbox
        - ``inline`` -- display the checkboxes inline?
        - ``optionNumber`` -- option number of inline
        - ``htmlId`` -- htmlId
        - ``inlineHelpText`` -- inline and block level support for help text that appears around form controls
        - ``blockHelpText`` -- a longer block of help text that breaks onto a new line and may extend beyond one line
        - ``disabled`` -- add the disabled attribute on an input to prevent user input
        - ``checked`` -- the default checked/unchecked state of the box

    **Return:**
        - ``checkbox`` -- the checkbox
    """
    if inline is True:
        inline = "inline"
        optionNumber = "option%(optionNumber)s" % locals()
    else:
        inline = ""
        optionNumber = ""

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

    if not htmlId:
        htmlId = ""
        name = ""
    else:
        name = """name="%(htmlId)s" """ % locals()

    if not checked:
        checked = ""
    else:
        checked = "checked"

    checkbox = """
        <label class="checkbox %(inline)s">
          <input type="checkbox" %(name)s value="%(optionNumber)s" id="%(htmlId)s %(disabledId)s" %(disabled)s %(checked)s>
          %(optionText)s
        </label>%(inlineHelpText)s%(blockHelpText)s""" % locals()

    return checkbox
