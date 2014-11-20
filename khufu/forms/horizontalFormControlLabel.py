# encoding: utf-8
from . import *

# LAST MODIFIED : April 16, 2013
# CREATED : April 16, 2013
# AUTHOR : DRYX


def horizontalFormControlLabel(
        labelText="",
        forId=False,
        sideLabel=False,
        location="left"):
    """set a horizontal form label

    **Key Arguments:**
        - ``labelText`` -- the label text
        - ``forId`` -- what is the label for (id of the associated object)?

    **Return:**
        - ``horizontalFormRowLabel`` -- the horizontalFormRowLabel
    """
    if forId is False:
        forId = ""

    if sideLabel:
        sideLabel = "sideLabel"
    else:
        sideLabel = ""

    horizontalFormRowLabel = """<label class="control-label %(sideLabel)s %(location)s" for="%(forId)s">%(labelText)s</label>""" % locals(
    )

    return horizontalFormRowLabel

