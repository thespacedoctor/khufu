# encoding: utf-8
from . import *


def searchForm(
        buttonText="",
        span=2,
        inlineHelpText=False,
        blockHelpText=False,
        focusedInputText=False,
        htmlId=False):
    """
    *Generate a search-form - TBS style*

    **Key Arguments:**
        - ``buttonText`` -- the button text
        - ``span`` -- column span
        - ``inlineHelpText`` -- inline and block level support for help text that appears around form controls
        - ``blockHelpText`` -- a longer block of help text that breaks onto a new line and may extend beyond one line
        - ``focusedInputText`` -- make the input focused by providing some initial editable input text
        - ``htmlId`` -- htmlId

    **Return:**
        - ``searchForm`` -- the search-form
    """
    if span:
        span = "span%(span)s" % locals()
    else:
        span = ""

    if not focusedInputText:
        focusedInputText = ""
        focusId = ""
    else:
        focusId = "focusedInput"

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

    if not htmlId:
        htmlId = ""

    searchForm = """
    <form class="form-search">
    <div class="input-append">
      <input type="text" class="search-query %(span)s" id="%(htmlId)s"  id="%(focusId)s" value="%(focusedInputText)s">
      <button type="submit" class="btn">%(buttonText)s</button>
            %(inlineHelpText)s%(blockHelpText)s
    </div>
    </form>""" % locals()

    return searchForm
