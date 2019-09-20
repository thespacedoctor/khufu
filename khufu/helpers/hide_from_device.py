# encoding: utf-8
from . import *


def hide_from_device(
        content="",
        onPhone=True,
        onTablet=True,
        onDesktop=True):
    """
    *hide from device)*

    **Key Arguments:**
        - ``content`` - content to hide/show
        - ``onPhone`` - onPhone?
        - ``onTablet`` - onTablet?
        - ``onDesktop`` - onDesktop?

    **Return:**
        - ``span`` -- span containings content with show/hide parameters
    """

    phoneClass = ""
    tabletClass = ""
    desktopClass = ""
    if onPhone:
        if onTablet:
            if not onDesktop:
                desktopClass = "hidden-desktop"
        else:
            if not onDesktop:
                phoneClass = "visible-phone"
            else:
                tabletClass = "hidden-tablet"
    else:
        if onTablet:
            if not onDesktop:
                tabletClass = "visible-tablet"
            else:
                phoneClass = "hidden-phone"
        else:
            desktopClass = "visible-desktop"

    span = """<span class="%(phoneClass)s %(tabletClass)s %(desktopClass)s">%(content)s</span>""" % locals(
    )
    return span
