# encoding: utf-8
from . import *


def emphasizeText(
        style="em",
        text=""):
    """
    *Get HTML's default emphasis tags with lightweight styles.*

    **Key Arguments:**
        - ``style`` -- the emphasis tag [ "small" | "strong" | "em" ]
        - ``text`` -- the text to emphasise

    **Return:**
        - ``emphasizeText`` -- the emphasized text
    """
    emphasizeText = """
        <%(style)s>
            %(text)s
        </%(style)s>""" % locals()

    return emphasizeText
