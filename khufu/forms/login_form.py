#!/usr/local/bin/python
# encoding: utf-8
"""
login_form.py
=============
:Summary:
    Login Form (mainly to be used in Pyramid apps)

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


class login_form():

    """
    The worker class for the login_form module

    **Key Arguments:**
        - ``log`` -- logger
        - ``iconPath`` -- path to webapp icon

    **Todo**
        - @review: when complete, clean login_form class
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract class to another module
    """
    # Initialisation
    # 1. @flagged: what are the unique attrributes for each object? Add them
    # to __init__

    def __init__(
        self,
        log,
        iconPath
    ):
        self.log = log
        log.debug("instansiating a new 'login_form' object")
        self.iconPath = iconPath

        # xt-self-arg-tmpx

        # 2. @flagged: what are the default attrributes each object could have? Add them to variable attribute set here
        # Variable Data Atrributes

        # 3. @flagged: what variable attrributes need overriden in any baseclass(es) used
        # Override Variable Data Atrributes

        # Initial Actions
        self.icon = khufu.image(
            src=iconPath,  # [ industrial | gray | social ]
            href=False,
            display="polaroid",  # [ rounded | circle | polaroid | False ]
            pull=False,  # [ "left" | "right" | "center" | False ]
            htmlClass=False,
            width=False
        )

        return None

    def close(self):
        del self
        return None

    # 4. @flagged: what actions does each object have to be able to perform? Add them here
    # Method Attributes
    def get(self):
        """get the login_form object

        **Return:**
            - ``login_form``

        **Todo**
            - @review: when complete, clean get method
            - @review: when complete add logging
        """
        self.log.info('starting the ``get`` method')

        login_form = "nice form"
        formContent = self._setup_form()

        self.log.info('completed the ``get`` method')
        return formContent

    def _setup_form(
            self):
        """ setup loging form

        **Key Arguments:**
            # -

        **Return:**
            - ``formContent`` -- content of the login form

        **Todo**
            - @review: when complete, clean _setup_form method
            - @review: when complete add logging
        """
        self.log.info('starting the ``_setup_form`` method')

        textInput = khufu.formInput(
            # [ text | password | datetime | datetime-local | date | month | time | week | number | float | email | url | search | tel | color ]
            ttype='text',
            placeholder='username',
            span=12,
            htmlId="username",
            searchBar=True,
            pull=False,
            prepend=False,
            append=False,
            button1=False,
            button2=False,
            prependDropdown=False,
            appendDropdown=False,
            inlineHelpText=False,
            blockHelpText=False,
            focusedInputText=False,
            required=True,
            disabled=False
        )
        textInput = khufu.controlRow(
            inputList=[textInput, ]
        )
        textLabel = khufu.horizontalFormControlLabel(
            labelText='',
            forId="username"
        )
        username = khufu.horizontalFormControlGroup(
            content=textInput,
            validationLevel=False
        )

        textInput = khufu.formInput(
            # [ text | password | datetime | datetime-local | date | month | time | week | number | float | email | url | search | tel | color ]
            ttype='password',
            placeholder='password',
            span=12,
            htmlId="password",
            searchBar=True,
            pull=False,
            prepend=False,
            append=False,
            button1=False,
            button2=False,
            prependDropdown=False,
            appendDropdown=False,
            inlineHelpText=False,
            blockHelpText=False,
            focusedInputText=False,
            required=True,
            disabled=False
        )
        textInput = khufu.controlRow(
            inputList=[textInput, ]
        )
        textLabel = khufu.horizontalFormControlLabel(
            labelText='',
            forId="password"
        )
        password = khufu.horizontalFormControlGroup(
            content=textInput,
            validationLevel=False
        )

        submit = khufu.button(
            buttonText='login',
            # [ default | primary | info | success | warning | danger | inverse | link ]
            buttonStyle='info',
            buttonSize='default',  # [ large | default | small | mini ]
            htmlId=False,
            href=False,
            pull=False,  # right, left, center
            submit=True,
            block=False,
            disable=False,
            postInBackground=False,
            dataToggle=False,  # [ modal ]
            popover=False
        )

        submit = khufu.horizontalFormControlGroup(
            content=submit,
            validationLevel=False
        )

        # submit = khufu.grid_column(
        # span=12,  # 1-12
        # offset=0,  # 1-12
        #     content=submit,
        # pull=False,  # ["right", "left", "center"]
        #     htmlId=False,
        #     htmlClass=False,
        #     onPhone=True,
        #     onTablet=True,
        #     onDesktop=True
        # )

        # xkhufu-tmpx-form-control-group
        # xkhufu-horizontal-form-item
        formContent = khufu.form(
            # list of control groups
            content=self.icon + username + password + submit,
            # [ "inline" | "horizontal" | "search" | "navbar-form" | "navbar-search" ]
            formType='inline',
            navBarPull=False,  # [ false | right | left ],
            postToScript="",
            htmlId=False,
            postInBackground=False,
            htmlClass=False,
            redirectUrl=False,
            span=False,
            offset=False
        )

        self.log.info('completed the ``_setup_form`` method')
        return formContent

    # use the tab-trigger below for new method
    # xt-class-method

    # 5. @flagged: what actions of the base class(es) need ammending? ammend them here
    # Override Method Attributes
    # method-override-tmpx

# xt-class-tmpx


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# xt-worker-def

# use the tab-trigger below for new function
# xt-def-with-logger

###################################################################
# PRIVATE (HELPER) FUNCTIONS                                      #
###################################################################

if __name__ == '__main__':
    main()
