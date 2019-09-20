# encoding: utf-8
from . import *


def select(
        optionList=[],
        valueList=False,
        multiple=False,
        span=2,
        htmlId=False,
        htmlClass=False,
        inlineHelpText=False,
        blockHelpText=False,
        required=False,
        disabled=False,
        popover=False,
        extraAttributeTupleList=False,
        defaultOption=False):
    """
    *Generate a select - TBS style*

    **Key Arguments:**
        - ``optionList`` -- the list of options
        - ``multiple`` -- display all the options at once?
        - ``span`` -- column span
        - ``htmlId`` -- the html id of the element
        - ``inlineHelpText`` -- inline and block level support for help text that appears around form controls
        - ``blockHelpText`` -- a longer block of help text that breaks onto a new line and may extend beyond one line
        - ``required`` -- required attribute if the field is not optional
        - ``disabled`` -- add the disabled attribute on an input to prevent user input
        - ``popover`` -- add helper text to the select
        - ``defaultOption`` -- option to select as default

    **Return:**
        - ``select`` -- the select
    """
    if not htmlId:
        htmlId = ""

    if not htmlClass:
        htmlClass = ""

    extraAttributes = ""
    if extraAttributeTupleList:
        for attributeTuple in extraAttributeTupleList:
            attr = attributeTuple[0]
            val = attributeTuple[1]
            if isinstance(val, str) or isinstance(val, unicode):
                val = '"%(val)s"' % locals()
            extraAttributes = """%(extraAttributes)s %(attr)s=%(val)s """ % locals(
            )

    if not valueList:
        valueList = optionList

    if multiple is True:
        multiple = """multiple="multiple" """
    else:
        multiple = ""

    if span:
        span = "span%(span)s" % locals()
    else:
        span = ""

    if popover is False:
        popover = ""

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

    options = ""
    for o, v in zip(optionList, valueList):
        if defaultOption and defaultOption == o:
            options = """%(options)s <option value="%(v)s" selected="selected">%(o)s</option>""" % locals()
        else:
            options = """%(options)s <option value="%(v)s">%(o)s</option>""" % locals()

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

    select = """
        <select %(multiple)s name="%(htmlId)s" class="%(span)s %(htmlClass)s" %(popover)s id="%(disabledId)s%(htmlId)s" %(required)s %(disabled)s %(extraAttributes)s>
            %(options)s
        </select>%(inlineHelpText)s%(blockHelpText)s
        """ % locals()

    return select
