# encoding: utf-8
from . import *


def htmlDocument(
        contentType=False,
        content='',
        attachmentSaveAsName=False):
    """
    *The doctype and html tags*

    **Key Arguments:**
        - ``content`` -- the head and body of the html page
        - ``attachmentSaveAsName`` -- save file as this name instead of opening in browser

    **Return:**
        - ``contentType`` -- the content type [ "text/html" ]
        - ``doctype`` -- the HTML5 doctype
    """

    if attachmentSaveAsName is not False:
        contentType = """Content-Disposition: attachment; filename=%(attachmentSaveAsName)s""" % locals(
        )
    elif not contentType:
        contentType = ""
    else:
        contentType = "Content-type: %(contentType)s" % locals()

    content = content.strip()

    if "text/plain" in contentType or "text/csv" in contentType or attachmentSaveAsName is not False:
        htmlDocument = \
            """%(contentType)s\n
%(content)s
""" % locals()
    else:
        htmlDocument = \
            """%(contentType)s\n
            <!DOCTYPE html>
            <html lang="en">
                %(content)s
            </html>
        """ \
            % locals()
    return htmlDocument.strip()
