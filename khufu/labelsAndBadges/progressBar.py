# encoding: utf-8
from . import *


def progressBar(
        barStyle="plain",
        precentageWidth="10",
        barLevel="info"):
    """
    *Generate a progress bar - TBS style*

    **Key Arguments:**
        - ``barStyle`` -- style of the progress bar [ "plain" | "striped" | "striped-active" ]
        - ``precentageWidth`` -- the current progress of the bar
        - ``barLevel`` -- the level color of the bar [ "info" | "warning" | "success" | "error" ]

    **Return:**
        - ``progressBar`` -- the progressBar
    """
    barLevel = "progress-%(barLevel)s" % locals()

    if barStyle == "striped":
        barStyle = "progress-striped"
    elif barStyle == "striped-active":
        barStyle = "progress-striped active"
    else:
        barStyle = ""

    progressBar = """
        <div class="progress %(barLevel)s %(barStyle)s">
          <div class="bar" style="width: %(precentageWidth)s%%;"></div>
        </div>""" % locals()

    return progressBar
