# CREATED : 20130508


def well(
        wellText='',
        wellSize='default',
        htmlId=False,
        htmlClass=False):
    """ *Get well. Use the well as a simple effect on an element to give it an inset effect.*

    **Key Arguments:**
        - ``wellText`` -- the text to be displayed in the well
        - ``wellSize`` -- the size of the well [ "default" | "large" | "small" ]

    **Return:**
        - ``well`` -- the well """

    if htmlId is False:
        htmlId = ""
    else:
        htmlId = """id="%(htmlId)s" """ % locals()

    if htmlClass is False:
        htmlClass = ""

    if wellSize == 'default':
        wellSize = ''
    else:
        wellSize = 'well-%(wellSize)s' % locals()
    well = """
        <div class="well %(wellSize)s %(htmlClass)s" %(htmlId)s>
            %(wellText)s
        </div>""" % locals()
    return well
