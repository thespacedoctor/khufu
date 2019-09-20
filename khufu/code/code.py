# encoding: utf-8
from . import *


def code(
        content="",
        inline=True,
        scroll=False):
    """
    *Generate a code section*

    **Key Arguments:**
        - ``content`` -- the content of the code block
        - ``inline`` -- inline or block?
        - ``scroll`` -- give the block a scroll bar on y-axis?

    **Return:**
        - ``code`` -- the code section
    """
    if scroll:
        scroll = "pre-scrollable"
    else:
        scroll = ""

    if inline:
        code = """<code>%(content)s</code>""" % locals()
    else:
        code = """
            <pre class="%(scroll)s"><code>%(content)s</code></pre>""" % locals()

    return code
