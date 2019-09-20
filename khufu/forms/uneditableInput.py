# encoding: utf-8
from . import *


def uneditableInput(
        placeholder="",
        span=2,
        inlineHelpText=False,
        blockHelpText=False):
    """
    *Generate a uneditableInput - TBS style*

    **Key Arguments:**
        - ``placeholder`` -- the placeholder text
        - ``span`` -- column span
        - ``inlineHelpText`` -- inline and block level support for help text that appears around form controls
        - ``blockHelpText`` -- a longer block of help text that breaks onto a new line and may extend beyond one line

    **Return:**
        - ``uneditableInput`` -- an uneditable input - the user can see but not interact
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

    uneditableInput = """
        <span class="%(span)s uneditable-input">
            %(placeholder)s
        </span>%(inlineHelpText)s%(blockHelpText)s""" % locals()

    return uneditableInput
