# encoding: utf-8
from . import *


def coloredText(
        text="",
        color="red",
        htmlClass="",
        pull=False,
        size=False,
        addBackgroundColor=False):
    """
    *Colour text a given colour*

    **Key Arguments:**
        - ``text`` -- the text to color
        - ``color`` -- the color
        - ``htmlClass`` -- the class for the text
        - ``size`` -- the relative size of the text
        - ``addBackgroundColor`` -- add a complimentary background color to the text

    **Return:**
        - ``text`` -- the coloured text span
    """
    if pull is not False:
        pull = """pull-%(pull)s""" % locals()
    else:
        pull = ""

    if size is not False:
        size = """size-%(size)s""" % locals()
    else:
        size = ""

    if addBackgroundColor is not False:
        addBackgroundColor = "addBackground"
    else:
        addBackgroundColor = ""

    text = """<span class="colortext %(color)s %(addBackgroundColor)s %(htmlClass)s %(pull)s %(size)s">%(text)s</span>""" % locals(
    )

    return text
