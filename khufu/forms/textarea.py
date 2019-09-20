# encoding: utf-8
from . import *


def textarea(
        rows="",
        span=2,
        placeholder="",
        htmlId=False,
        inlineHelpText=False,
        blockHelpText=False,
        focusedInputText=False,
        required=False,
        disabled=False,
        prepopulate=False):
    """
    *Generate a textarea - TBS style*

    **Key Arguments:**
        - ``rows`` -- the number of rows the text area should span
        - ``span`` -- column span
        - ``placeholder`` -- the placeholder text
        - ``htmlId`` -- html id for item
        - ``inlineHelpText`` -- inline and block level support for help text that appears around form controls
        - ``blockHelpText`` -- a longer block of help text that breaks onto a new line and may extend beyond one line
        - ``focusedInputText`` -- make the input focused by providing some initial editable input text
        - ``required`` -- required attribute if the field is not optional
        - ``disabled`` -- add the disabled attribute on an input to prevent user input

    **Return:**
        - ``textarea`` -- the textarea
    """
    if span:
        span = "span%(span)s" % locals()
    else:
        span = ""

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

    if not focusedInputText:
        focusedInputText = ""
        focusId = ""
    else:
        focusId = "focusedInput"

    if required:
        required = """required"""
    else:
        required = ""

    if disabled:
        disabled = """disabled"""
        disabledId = "disabledId"
    else:
        disabled = ""
        disabledId = ""

    if not htmlId:
        htmlId = ""
        name = "textarea"
    else:
        name = htmlId

    if prepopulate is False:
        prepopulate = ""

    textarea = """<textarea rows="%(rows)s" class="%(span)s" id="%(htmlId)s%(focusId)s%(disabledId)s" value="%(focusedInputText)s" %(required)s %(disabled)s placeholder="%(placeholder)s" name="%(name)s">%(prepopulate)s</textarea>%(inlineHelpText)s%(blockHelpText)s""" % locals(
    )

    return textarea
