# CREATED : February 25, 2014


def popover(
        tooltip=False,
        placement=False,
        trigger=False,
        title=False,
        content=False,
        delay=200,
        after=False):
    """
    *popover to provide helper text or some secondary info about an element*

    **Key Arguments:**
        - ``tooltip`` -- use tooltip instead of popover
        - ``placement`` -- direction popover expands into [ top | bottom | left | right ]
        - ``trigger`` -- the trigger for the popover [ False | click | hover | focus | manual ]
        - ``title`` -- the popover title
        - ``content`` -- the popover content
        - ``delay`` -- delay in ms
        - ``after`` -- place the div required by the 


    **Return:**
        - ``popover`` - the popover helper text to be added to an element

    .. todo::

        - [ ] when complete, clean popover function
        - [ ] when complete add logging
        - [ ] when complete, decide whether to abstract function to another module
    """

    if tooltip is False:
        tooltip = "popover"
        # title = """data-original-title="%(title)s" """ % locals()
    else:
        tooltip = "tooltip"
        content = False

    if title:
        title = title.replace('"', "'")
    if content:
        content = content.replace('"', "'")

    popover = """rel="%(tooltip)s" data-container="body" data-placement="%(placement)s" """ % locals()
    if trigger is not False:
        popover = """%(popover)s data-trigger="%(trigger)s" """ % locals()
    if title is not False:
        popover = """%(popover)s data-original-title="%(title)s" """ % locals()
    if content is not False:
        popover = """%(popover)s data-content="%(content)s" """ % locals()
    if delay is not False:
        popover = """%(popover)s data-delay="%(delay)s" """ % locals()

    if (title and "<" in title and ">" in title) or (content and "<" in content and ">" in content):
        popover = """%(popover)s data-html=true """ % locals()

    return popover
