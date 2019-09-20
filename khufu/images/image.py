# encoding: utf-8
from . import *


def image(
        src="http://placehold.it/200x200",
        href=False,
        display=False,  # [ rounded | circle | polaroid ]
        pull="left",  # [ "left" | "right" | "center" ]
        htmlClass=False,
        htmlId=False,
        thumbnail=False,
        width=False,
        height=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True,
        clickToModal=False,
        openInNewTab=False,
        modal=False):
    """Create an HTML image (with ot without link).
    Based on the Twitter bootstrap setup.

    **Key Arguments:**
        - ``src`` -- image url
        - ``href`` -- image link url
        - ``display`` -- how the image is to be displayed [ rounded | circle | polaroid ]
        - ``pull`` -- how to align the image if within a <div> [ "left" | "right" | "center" ]
        - ``htmlId`` -- the id of the image
        - ``htmlClass`` -- the class of the image
        - ``width`` -- the width of the image
        - ``onPhone`` -- does this container get displayed on a phone sized screen
        - ``onTablet`` -- does this container get displayed on a tablet sized screen
        - ``onDesktop`` -- does this container get displayed on a desktop sized screen
        - ``clickToModal`` -- if you want to display the image in a modal when clicked?
        - ``openInNewTab`` -- open image link in new tab?
        - ``modal`` -- is this linked to a modal?

    **Return:**
        - ``image`` - the formatted image
    """
    falseList = [thumbnail, pull]
    for i in range(len(falseList)):
        if not falseList[i]:
            falseList[i] = ""

    [thumbnail, pull] = falseList

    if thumbnail is True:
        thumbnail = "thumbnail"

    if pull:
        pull = "pull-%(pull)s" % locals()

    if not display:
        display = ""
    else:
        display = """img-%(display)s""" % locals()
    if not htmlClass:
        htmlClass = ""
    if width:
        width = """width=%(width)s""" % locals()
    else:
        width = ""

    if height:
        height = """height=%(height)s""" % locals()
    else:
        height = ""

    if onPhone:
        onPhone = ""
    else:
        onPhone = "hidden-phone"
    if onTablet:
        onTablet = ""
    else:
        onTablet = "hidden-tablet"
    if onDesktop:
        onDesktop = ""
    else:
        onDesktop = "hidden-desktop"

    if htmlId:
        htmlId = """id="%(htmlId)s" """ % locals()
    else:
        htmlId = ""

    if clickToModal is False:
        clickToModal = ""
    else:
        clickToModal = "clickToModal"

    if modal:
        modal = 'data-toggle=modal'
    else:
        modal = ""

    if "holder.js" in src:
        src = """data-src="%(src)s" """ % locals()
    else:
        src = """src="%(src)s" """ % locals()

    image = """<img %(src)s class="%(display)s %(htmlClass)s %(onPhone)s %(onTablet)s %(onDesktop)s %(pull)s %(clickToModal)s" %(htmlId)s %(width)s %(height)s >""" % locals(
    )

    if openInNewTab is not False:
        openInNewTab = """target="_blank" """
    else:
        openInNewTab = ""

    if href:
        image = """<a href="%(href)s" class="%(thumbnail)s %(onPhone)s %(onTablet)s %(onDesktop)s %(pull)s" %(htmlId)s %(openInNewTab)s %(modal)s>%(image)s</a>""" % locals(
        )

    return image
