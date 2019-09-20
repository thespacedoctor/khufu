#!/usr/local/bin/python
# encoding: utf-8
"""
*Simple Login Page*

:Author:
    David Young

:Date Created:
    November 20, 2014
"""
import sys
import os
from fundamentals import tools, times
import khufu


class login_page():

    """
    *The worker class for the login_page module*

    **Key Arguments:**
        - ``log`` -- logger
        - ``mainCssFilePath`` -- the filepath of the main CSS file
        - ``jsFilePath`` -- the filepath of the main JS file
        - ``pageTitle`` -- pageTitle
        - ``iconPath`` -- webapp icon path
        - ``came_from`` -- the url this login page was triggered from
        - ``message`` -- message to display as notification
    """

    def __init__(
            self,
            log,
            mainCssFilePath="/static/styles/main.css",
            jsFilePath="/static/js/main-ck.js",
            pageTitle="Login",
            iconPath="",
            came_from="/",
            message=""
    ):
        self.log = log
        log.debug("instansiating a new 'login_page' object")
        self.mainCssFilePath = mainCssFilePath
        self.jsFilePath = jsFilePath
        self.pageTitle = pageTitle
        self.iconPath = iconPath
        self.came_from = came_from
        self.message = message

        # xt-self-arg-tmpx

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

    def get(self):
        """
        *get the login_page object*

        **Return:**
            - ``login_page`` -- the html login page
        """
        self.log.debug('starting the ``get`` method')

        # CREATE THE WEBPAGE
        login_page = self.webapge
        # CLEAR MESSAGE
        self.message = ""

        self.log.debug('completed the ``get`` method')
        return login_page

    def _build_webapge_scaffolding(
            self):
        """
        *build webapge scaffolding*

        **Key Arguments:**

        **Return:**
            - ``webpage`` -- the html login page
        """
        self.log.debug('starting the ``_build_webapge_scaffolding`` method')

        head = khufu.head(
            relativeUrlBase=False,
            mainCssFilePath=self.mainCssFilePath,
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
            jsFilePath=self.jsFilePath
        )

        webpage = khufu.htmlDocument(
            contentType=False,
            content="%(head)s %(body)s" % locals()
        )

        self.log.debug('completed the ``_build_webapge_scaffolding`` method')
        return webpage
