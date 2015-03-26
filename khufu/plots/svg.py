# encoding: utf-8
from . import *

#!/usr/bin/env python
# encoding: utf-8
"""
svg.py
===========
:Summary:
    Add an SVG chart placeholder to the HTML of your webpage

:Author:
    David Young

:Date Created:
    May 9, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
"""
################# GLOBAL IMPORTS ####################
import sys
import os
from docopt import docopt
from dryxPython import commonutils as dcu

# LAST MODIFIED : May 9, 2014
# CREATED : May 9, 2014
# AUTHOR : DRYX


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
    """svg

    **Key Arguments:**
        - ``htmlClass`` -- the extra html classes required
        - ``disable`` -- disable the plot (can enable via javascript)
        - ``htmlId`` -- the html id if required
        - ``csvUrl`` -- url to a csv file/csv data
        - ``chartType`` -- the type of chart required (determines which javascript function to trigger)
        - ``span`` -- span of chart area

    **Return:**
        - ``svg`` -- the svg element

    **Todo**
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

    svg = """<svg class="chart %(htmlClass)s  %(span)s" %(htmlId)s chartType="%(chartType)s" data-src="%(dataUrl)s" disable="%(disable)s" %(height)s></svg>""" % locals(
    )

    return svg


if __name__ == '__main__':
    main()
