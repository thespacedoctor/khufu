# encoding: utf-8
from . import *


def alert(alertText='',
          alertHeading="",
          extraPadding=False,
          alertLevel="warning"):
    """ *Generate a alert - TBS style*

    **Key Arguments:**
        - ``alertText`` -- the text to be displayed in the alert
        - ``extraPadding`` -- for longer messages, increase the padding on the top and bottom of the alert wrapper
        - ``alertLevel`` -- the level of the alert [ "warning" | "error" | "success" | "info" ]

    **Return:**
        - ``alert`` -- the alert """

    falseList = [extraPadding, ]
    for i in range(len(falseList)):
        if not falseList[i]:
            falseList[i] = ""
    [extraPadding, ] = falseList

    if alertLevel == "default":
        alertLevel = ""
    else:
        alertLevel = "alert-%(alertLevel)s" % locals()

    if extraPadding:
        extraPadding = "alert-block"
        alertHeading = "<h4>%(alertHeading)s</h4>" % locals()
    else:
        alertHeading = "<strong>%(alertHeading)s</strong>" % locals()

    alert = \
        """
        <div class="alert %(extraPadding)s %(alertLevel)s">
          <button type="button" class="close" data-dismiss="alert">&times;</button>
          %(alertHeading)s %(alertText)s
        </div>""" \
        % locals()
    return alert
