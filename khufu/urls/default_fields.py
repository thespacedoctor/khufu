#!/usr/bin/env python
# encoding: utf-8
"""
default_fields.py
=================
:Summary:
    Pass a dictionary of the default url fields and their default values to be added to locals() of the calling module

:Author:
    David Young

:Date Created:
    May 28, 2014

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

# LAST MODIFIED : May 28, 2014
# CREATED : May 28, 2014
# AUTHOR : DRYX


def default_fields():
    """default feilds

    **Return:**
        - ``fieldDict`` -- a dictionary of { fieldName, defaultValue }

    **Todo**
    """
    fieldDict = {
        "sortBy": False,
        "sortDesc": False,
        "pageName": False,
        "pageId": False,
        "tagName": False,
        "settingsFile": 1
    }
    return fieldDict


if __name__ == '__main__':
    main()
