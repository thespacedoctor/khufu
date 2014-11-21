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
"""
################# GLOBAL IMPORTS ####################
import sys
import os
from docopt import docopt
from dryxPython import logs as dl
from dryxPython import commonutils as dcu
from dryxPython.projectsetup import setup_main_clutil
import khufu


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
        - ``came_from`` -- the url this login page was triggered from
        - ``message`` -- message to display as notification

    **Todo**
    """
    # Initialisation

    def __init__(
            self,
            log,
            mainCssFileName="main.css",
            jsFileName="main-ck.js",
            pageTitle="Login",
            iconPath="",
            came_from="/",
            message=""
    ):
        self.log = log
        log.debug("instansiating a new 'login_page' object")
        self.mainCssFileName = mainCssFileName
        self.jsFileName = jsFileName
        self.pageTitle = pageTitle
        self.iconPath = iconPath
        self.came_from = came_from
        self.message = message

        # xt-self-arg-tmpx

        # Initial actions
        # create the form
        formContent = khufu.forms.login_form(
            self.log,
            self.iconPath,
            self.message
        )
        self.formContent = formContent.get()
        self.webapge = self._build_webapge_scaffolding()

        return None

    def close(self):
        del self
        return None

    # Method Attributes
    def get(self):
        """get the login_page object

        **Return:**
            - ``login_page`` -- the html login page

        **Todo**
        """
        self.log.info('starting the ``get`` method')

        # create the webpage
        login_page = self.webapge
        # clear message
        self.message = ""

        self.log.info('completed the ``get`` method')
        return login_page

    def _build_webapge_scaffolding(
            self):
        """ build webapge scaffolding

        **Key Arguments:**

        **Return:**
            - ``webpage`` -- the html login page

        **Todo**
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


if __name__ == '__main__':
    main()
