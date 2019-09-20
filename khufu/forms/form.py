# encoding: utf-8
from . import *


def form(
        content="",
        formType="inline",
        postToScript="",
        htmlId=False,
        htmlClass=False,
        navBarPull=False,
        postInBackground=False,
        redirectUrl=False,
        span=False,
        offset=False,
        openInNewTab=False):
    """
    *Generate a form - TBS style*

    **Key Arguments:**
        - ``content`` -- the content
        - ``formType`` -- the type if the form required [ "inline" | "horizontal" | "search" | "navbar-form" | "navbar-search" ]
        - ``postToScript`` -- the script to post the form values to
        - ``htmlId`` -- the id for the form
        - ``navBarPull`` -- align the form is in a navBar [ false | right | left ]
        - ``postInBackground`` -- submit form in background without refreshing page
        - ``redirectUrl`` -- url to redirect to after form is submitted

    **Return:**
        - ``inlineForm`` -- the inline form
    """
    falseList = [navBarPull, ]

    for i in range(len(falseList)):
        if not falseList[i]:
            falseList[i] = ""

    [navBarPull, ] = falseList

    if span is False:
        span = ""
    else:
        span = "span%(span)s" % locals()

    if offset is False:
        offset = ""
    else:
        offset = "offset%(offset)s" % locals()

    if not htmlClass:
        htmlClass = ""

    if postInBackground is True:
        postInBackground = "postInBackground"
    else:
        postInBackground = ""

    if redirectUrl is not False:
        redirectUrl = formInput(
            # [ text | password | datetime | datetime-local | date | month | time | week | number | email | url | search | tel | color ]
            ttype='text',
            htmlId="redirectURL",
            defaultValue=redirectUrl,
            hidden=True
        )
    else:
        redirectUrl = ""

    if navBarPull:
        navBarPull = "pull-%(navBarPull)s" % locals()

    thisList = ["inline", "horizontal", "search"]
    if formType in thisList:
        formType = """form-%(formType)s""" % locals()

    htmlInput = ""
    if formType == "navbar-search":
        htmlInput = """%(htmlInput)s<input type="text" class="search-query" placeholder="search">""" % locals()

    if htmlId:
        htmlId = """id="%(htmlId)s" """ % locals()
    else:
        htmlId = ""

    if openInNewTab is not False:
        openInNewTab = """ target="_blank" """

    form = """<form class="%(formType)s %(navBarPull)s %(postInBackground)s %(span)s %(offset)s %(htmlClass)s" %(htmlId)s action="%(postToScript)s" method="post" %(openInNewTab)s>%(content)s%(htmlInput)s%(redirectUrl)s</form>""" % locals(
    )

    return form
