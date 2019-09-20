# encoding: utf-8
from . import *
import sys
import os


def svg(
    htmlClass=False,
    dataUrl="#",
    dataFormat="json",
    disable=False,
    htmlId=False,
    chartType="",
    span=12,
    height=False
):
    """
    *svg*

    **Key Arguments:**
        - ``htmlClass`` -- the extra html classes required
        - ``disable`` -- disable the plot (can enable via javascript)
        - ``htmlId`` -- the html id if required
        - ``csvUrl`` -- url to a csv file/csv data
        - ``chartType`` -- the type of chart required (determines which javascript function to trigger)
        - ``span`` -- span of chart area

    **Return:**
        - ``svg`` -- the svg element
    """

    if not htmlClass:
        htmlClass = ""

    if htmlId:
        htmlId = """id="%(htmlId)s" """ % locals()
    else:
        htmlId = ""

    if disable:
        disable = "true"
    else:
        disable = "false"

    if span:
        span = "span%(span)s" % locals()
    else:
        span = ""

    if not height:
        height = ""
    elif height == "square":
        htmlClass += " square "
        height = ""
    else:
        height = """ height=%(height)s """ % locals()

    svg = """<svg class="chart %(htmlClass)s  %(span)s" %(htmlId)s chartType="%(chartType)s" data-src="%(dataUrl)s" disable="%(disable)s" %(height)s ></svg>""" % locals(
    )

    return svg
