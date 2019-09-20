#!/usr/bin/env python
# encoding: utf-8
"""
*Pass a dictionary of the default url fields and their default values to be added to locals() of the calling module*

:Author:
    David Young

:Date Created:
    May 28, 2014
"""
import sys
import os


def default_fields():
    """
    *default feilds*

    **Return:**
        - ``fieldDict`` -- a dictionary of { fieldName, defaultValue }
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
