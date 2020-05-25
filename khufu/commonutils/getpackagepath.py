#!/usr/local/bin/python
# encoding: utf-8
"""
*Get common file and folder paths for the host package*

:Author:
    David Young
"""
import sys
import os

def getpackagepath():
    """
    *getpackagepath*

    **Return**

    - ``packagePath`` -- path to the host package
    
    """

    moduleDirectory = os.path.dirname(__file__)
    packagePath = os.path.dirname(__file__) + "/../"

    return packagePath
