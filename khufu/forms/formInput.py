# encoding: utf-8
from . import *


def formInput(
        ttype="text",
        placeholder="",
        span=2,
        htmlId=False,
        searchBar=False,
        pull=False,
        prepend=False,
        append=False,
        button1=False,
        button2=False,
        prependDropdown=False,
        appendDropdown=False,
        inlineHelpText=False,
        blockHelpText=False,
        focusedInputText=False,
        rightText=False,
        required=False,
        disabled=False,
        defaultValue=False,
        hidden=False,
        divWrap=True):
    """
    *Generate a form input - TBS style*

    **Key Arguments:**
        - ``ttype`` -- [ text | password | datetime | datetime-local | date | month | time | week | number | float | email | url | search | tel | color ]
        - ``placeholder`` -- the placeholder text
        - ``span`` -- column span
        - ``htmlId`` -- html id
        - ``searchBar`` -- is this input a searchbar?
        - ``pull`` -- [ false | right | left ] align form
        - ``prepend`` -- prepend text to the input.
        - ``append`` -- append text to the input.
        - ``button1`` -- do you want a button associated with the input?
        - ``button2`` -- as above for a 2nd button
        - ``appendDropdown`` -- do you want a appended button-dropdown associated with the input?
        - ``prependDropdown`` -- do you want a prepended button-dropdown associated with the input?
        - ``inlineHelpText`` -- inline and block level support for help text that appears around form controls
        - ``blockHelpText`` -- a longer block of help text that breaks onto a new line and may extend beyond one line
        - ``focusedInputText`` -- make the input focused by providing some initial editable input text
        - ``required`` -- required attribute if the field is not optional
        - ``disabled`` -- add the disabled attribute on an input to prevent user input
        - ``defaultValue`` -- a default value to be passed to action script
        - ``hidden`` -- hide the CG from the user?
        - ``divWrap`` -- wrap in div

    **Return:**
        - ``input`` -- the input
    """
    prependContent = False
    appendContent = False
    inputId = False
    searchClass = False
    prependClass = False
    appendClass = False

    if hidden:
        hidden = u"""hidden"""
    else:
        hidden = u""

    falseList = [searchBar, span, prepend, prependContent, append,
                 appendContent, inputId, pull, htmlId, appendClass, prependClass]

    for i in range(len(falseList)):
        if not falseList[i]:
            falseList[i] = u""

    [searchBar, span, prepend, prependContent, append, appendContent,
        inputId, pull, htmlId, appendClass, prependClass] = falseList

    if pull:
        pull = u"pull-%(pull)s" % locals()

    if span:
        span = u"span%(span)s" % locals()

    if searchBar:
        searchClass = u"search-query"
    else:
        searchClass = u""

    if prepend:
        prependClass = u"input-prepend"
        prependContent = u"""<span class="add-on">%(prepend)s</span>""" % locals(
        )

    if append:
        appendClass = u"input-append"
        appendContent = u"""<span class="add-on">%(append)s</span>""" % locals()

    # if prepend:
    #     if append:
    #         inputId = "appendedPrependedInput "
    #     else:
    #         inputId = "prependedInput "
    # elif append:
    #     inputId = "appendedInput "

    if button1:
        appendClass = u"input-append"
        appendContent = button1
        # inputId = "appendedInputButton "

    if button2:
        appendClass = u"input-append"
        appendContent = u"""%(appendContent)s %(button2)s""" % locals()
        # inputId = "appendedInputButtons "

    if appendDropdown:
        appendClass = u"input-append"
        # inputId = "appendedDropdownButton "
        appendContent = u"""
        <div class="btn-group">
            %(appendDropdown)s
        </div>""" % locals()

    if prependDropdown:
        prependClass = u"input-prepend"
        # inputId = "prependedDropdownButton "
        prependContent = u"""
        <div class="btn-group">
            %(prependDropdown)s
        </div>""" % locals()

    step = u""
    if ttype == "float":
        step = u""" step="any" """
        ttype = u"number"

    if prependDropdown and appendDropdown:
        pass
        # inputId = "appendedPrependedDropdownButton "

    if inlineHelpText:
        inlineHelpText = u"""<span class="help-inline">%(inlineHelpText)s</span>""" % locals(
        )
    else:
        inlineHelpText = u""

    if blockHelpText:
        blockHelpText = u"""<span class="help-block">%(blockHelpText)s</span>""" % locals(
        )
    else:
        blockHelpText = u""

    if not focusedInputText:
        focusedInputText = u""
        focusId = u""
    else:
        focusedInputText = u"""value="%(focusedInputText)s" """ % locals()
        focusId = u"focusedInput "

    if required:
        required = u"""required"""
    else:
        required = u""

    if disabled:
        disabled = u"""disabled"""
        disabledId = u""
    else:
        disabled = u""
        disabledId = u""

    if defaultValue:
        if isinstance(defaultValue, str) or isinstance(defaultValue, unicode):
            defaultValue = defaultValue.replace('"', "\"")
            defaultValue = u'"%(defaultValue)s"' % locals()

        defaultValue = u"""value=%(defaultValue)s """ % locals()
    else:
        defaultValue = u""

    thisInput = u"""
    %(prependContent)s
    <input class="%(searchClass)s %(span)s" id="%(htmlId)s%(focusId)s%(disabledId)s" %(focusedInputText)s type="%(ttype)s" %(step)s placeholder="%(placeholder)s" %(required)s %(disabled)s name="%(htmlId)s" %(defaultValue)s>
    %(appendContent)s
    """ % locals()

    if rightText is not False:
        thisInput = u"""<label class="inline">%(thisInput)s%(rightText)s </label>""" % locals(
        )

    if divWrap:
        formInput = u"""
            <div class="%(prependClass)s %(appendClass)s %(hidden)s %(pull)s">
                
                %(thisInput)s 
                
            </div>%(inlineHelpText)s%(blockHelpText)s
            """ % locals()
    else:
        formInput = thisInput

    return formInput
