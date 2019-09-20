# encoding: utf-8
from . import *


def table(
        caption="",
        thead="",
        tbody="",
        striped=True,
        bordered=False,
        hover=True,
        condensed=False,
        span=False):
    """
    *Generate a table - TBS style*

    **Key Arguments:**
        - ``caption`` -- the table caption
        - ``thead`` -- the table head
        - ``tbody`` -- the table body
        - ``striped`` -- Adds zebra-striping to any odd table row
        - ``bordered`` -- Add borders and rounded corners to the table.
        - ``hover`` -- Enable a hover state on table rows within a <tbody>
        - ``condensed`` -- Makes tables more compact by cutting cell padding in half.

    **Return:**
        - ``table`` -- the table
    """
    if striped is True:
        striped = "table-striped"
    else:
        striped = ""

    if caption is False:
        caption = ""

    if bordered is True:
        bordered = ""
    else:
        bordered = "table-bordered"

    if hover is True:
        hover = "table-hover"
    else:
        hover = ""

    if span is False:
        span = ""
    else:
        span = "span%(span)s" % locals()

    if condensed is True:
        condensed = "table-condensed"
    else:
        condensed = ""

    table = """<table class="table %(striped)s %(bordered)s %(hover)s %(condensed)s %(span)s">%(thead)s%(tbody)s%(caption)s</table>""" % locals(
    )
    return table
