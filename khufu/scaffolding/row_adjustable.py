# encoding: utf-8
from . import *


def row_adjustable(
    span=12,
    offset=0,
    content='',
    htmlId=False,
    htmlClass=False,
    onPhone=True,
    onTablet=True,
    onDesktop=True
):
    """
    *row adjustable*

    **Key Arguments:**
        - ``span`` -- the relative width of the column
        - ``offset`` -- increase the left margin of the column by this amount
        - ``content`` -- content for the row
        - ``htmlId`` -- the id of the column
        - ``htmlClass`` -- the class of the column
        - ``onPhone`` -- does this column get displayed on a phone sized screen
        - ``onTablet`` -- does this column get displayed on a tablet sized screen
        - ``onDesktop`` -- does this column get displayed on a desktop sized screen

    **Return:**
        - ``row`` -- the adjustable row
    """

    column = grid_column(
        span=span,  # 1-12
        offset=offset,  # 1-12
        content=content
    )

    row = grid_row(
        responsive=True,
        columns=column,
        htmlId=htmlId,
        htmlClass=htmlClass,
        onPhone=onPhone,
        onTablet=onTablet,
        onDesktop=onDesktop
    )

    return row
