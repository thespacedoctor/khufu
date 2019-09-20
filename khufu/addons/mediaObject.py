# CREATED : 20130508


def mediaObject(
    displayType='div',
    imagePath='',
    headlineText='',
    otherContent=False,
    nestedMediaObjects=False,
):
    """ *Generate an abstract object style for building various types of components (like blog comments, Tweets, etc) that feature a left- or right-aligned image alongside textual content.*

    **Key Arguments:**
        - ``displayType`` -- the display style of the media object [ "div" | "li" ]
        - ``img`` -- the image to include
        - ``headlineText`` -- the headline text for the object
        - ``otherContent`` -- other content to be displayed inside the media object
        - ``nestedMediaObjects`` -- nested media objects to be appended

    **Return:**
        - ``media`` -- the media object """

    falseList = [nestedMediaObjects]

    for i in range(len(falseList)):
        if not falseList[i]:
            falseList[i] = ""

    [nestedMediaObjects] = falseList

    if not otherContent:
        otherContent = ""

    thisImage = images.image(
        src=imagePath,  # [ industrial | gray | social ]
        href=False,
        display="polaroid",  # [ rounded | circle | polaroid | False ]
        pull="left",  # [ "left" | "right" | "center" | False ]
        htmlClass=False,
        width=False
    )

    thisImage = """<img src="%(imagePath)s" class="pull-left" style="width: 128px;">""" % locals(
    )

    thisImage = images.image(
        src=imagePath,
        href=imagePath,
        display="polaroid",  # [ rounded | circle | polaroid ]
        pull="left",  # [ "left" | "right" | "center" ]
        htmlClass=False,
        htmlId=False,
        thumbnail=True,
        width=150,
        height=False,
    )

    mediaObject = \
        """
        <%(displayType)s class="media" id="  ">
            %(thisImage)s
            <div class="media-body">
                <h4 class="media-heading">%(headlineText)s</h4>
                %(otherContent)s
                <!-- Nested media object -->
                %(nestedMediaObjects)s
            </div>
        </%(displayType)s>""" \
        % locals()
    return mediaObject
