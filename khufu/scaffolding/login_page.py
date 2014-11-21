#!/usr/local/bin/python
# encoding: utf-8
"""
login_page.py
=============
:Summary:
    Simple Login Page

:Author:
    David Young

:Date Created:
    November 20, 2014

:dryx syntax:
    - ``_someObject`` = a 'private' object that should only be changed for debugging

:Notes:
    - If you have any questions requiring this script/module please email me: d.r.young@qub.ac.uk

:Tasks:
    @review: when complete pull all general functions and classes into dryxPython
"""
################# GLOBAL IMPORTS ####################
import sys
import os
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from dryxPython.projectsetup import setup_main_clutil
import khufu
# from ..__init__ import *

###################################################################
# CLASSES                                                         #
###################################################################


class login_page():

    """
    The worker class for the login_page module

    **Key Arguments:**
        - ``log`` -- logger
        - ``mainCssFileName`` -- the filename of the main CSS file
        - ``jsFileName`` -- the filename of the main JS file
        - ``pageTitle`` -- pageTitle
        - ``iconPath`` -- webapp icon path

    **Todo**
        - @review: when complete, clean login_page class
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract class to another module
    """
    # Initialisation
    # 1. @flagged: what are the unique attrributes for each object? Add them
    # to __init__

    def __init__(
            self,
            log,
            mainCssFileName="main.css",
            jsFileName="main-ck.js",
            pageTitle="Login",
            iconPath=""
    ):
        self.log = log
        log.debug("instansiating a new 'login_page' object")
        self.mainCssFileName = mainCssFileName
        self.jsFileName = jsFileName
        self.pageTitle = pageTitle
        self.iconPath = iconPath

        # xt-self-arg-tmpx

        # 2. @flagged: what are the default attrributes each object could have? Add them to variable attribute set here
        # Variable Data Atrributes

        # 3. @flagged: what variable attrributes need overriden in any baseclass(es) used
        # Override Variable Data Atrributes

        formContent = khufu.forms.login_form(
            self.log,
            self.iconPath
        )
        self.formContent = formContent.get()
        self.webapge = self._build_webapge_scaffolding()

        return None

    def close(self):
        del self
        return None

    # 4. @flagged: what actions does each object have to be able to perform? Add them here
    # Method Attributes
    def get(self):
        """get the login_page object

        **Return:**
            - ``login_page``

        **Todo**
            - @review: when complete, clean get method
            - @review: when complete add logging
        """
        self.log.info('starting the ``get`` method')

        login_page = self.webapge

        self.log.info('completed the ``get`` method')
        return login_page

    def _build_webapge_scaffolding(
            self):
        """ build webapge scaffolding

        **Key Arguments:**
            # -

        **Return:**
            - None

        **Todo**
            - @review: when complete, clean _build_webapge_scaffolding method
            - @review: when complete add logging
        """
        self.log.info('starting the ``_build_webapge_scaffolding`` method')

        head = khufu.head(
            relativeUrlBase=False,
            mainCssFileName='main_marshall.css',
            pageTitle=self.pageTitle,
            extras=''
        )

        pageContent = khufu.grid_row(
            responsive=True,
            columns=self.formContent,
            htmlId="login_row",
            htmlClass=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )

        body = khufu.body(
            navBar=False,
            content=pageContent,
            htmlId='',
            extraAttr='',
            relativeUrlBase=False,
            responsive=True,
            googleAnalyticsCode=False,
            jsFileName="main-ck.js"
        )

        webpage = khufu.htmlDocument(
            contentType=False,
            content="%(head)s %(body)s" % locals()
        )

        self.log.info('completed the ``_build_webapge_scaffolding`` method')
        return webpage

    # use the tab-trigger below for new method
    # xt-class-method

    # 5. @flagged: what actions of the base class(es) need ammending? ammend them here
    # Override Method Attributes
    # method-override-tmpx


if __name__ == '__main__':
    main()
