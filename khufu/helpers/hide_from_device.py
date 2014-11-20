# encoding: utf-8
from . import *

# LAST MODIFIED : June 26, 2014
# CREATED : June 26, 2014
# AUTHOR : DRYX


def hide_from_device(
        content="",
        onPhone=True,
        onTablet=True,
        onDesktop=True):
    """hide from device)

    **Key Arguments:**

        # copy usage method(s) here and select the following snippet from the command palette:
        # x-setup-docstring-keys-from-selected-usage-options

    **Return:**
        - None

    **Todo**
        - @review: when complete, clean hide_from_device) function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
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

