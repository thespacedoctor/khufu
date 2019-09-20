# encoding: utf-8
from . import *


def stackedProgressBar(
        barStyle="plain",
        infoWidth="10",
        successWidth="10",
        warningWidth="10",
        errorWidth="10"
):
    """
    *Generate a progress bar - TBS style*

    **Key Arguments:**
        - ``barLevel`` -- the level/color of progress [ "info" | "success" | "warning" | "danger"]
        - ``barStyle`` -- style of the progress bar [ "plain" | "striped" | "striped-active" ]
        - ``infoWidth`` -- the precentage width of the info level bar
        - ``successWidth`` -- the precentage width of the success level bar
        - ``warningWidth`` -- the precentage width of the warning level bar
        - ``errorWidth`` -- the precentage width of the error level bar

    **Return:**
        - ``progressBar`` -- the progressBar
    """
    if barStyle == "striped":
        barStyle = "progress-striped"
    elif barStyle == "striped-active":
        barStyle = "progress-striped active"
    else:
        barStyle = ""

    stackedProgressBar = """
        <div class="progress %(barStyle)s">
          <div class="bar bar-info" style="width: %(infoWidth)s%%;"></div>
          <div class="bar bar-success" style="width: %(successWidth)s%%;"></div>
          <div class="bar bar-warning" style="width: %(warningWidth)s%%;"></div>
          <div class="bar bar-danger" style="width: %(errorWidth)s%%;"></div>
        </div>""" % locals()
    return stackedProgressBar
