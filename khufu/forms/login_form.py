#!/usr/local/bin/python
# encoding: utf-8
"""
*Login Form (mainly to be used in Pyramid apps)*

:Author:
    David Young

:Date Created:
    November 20, 2014
"""
import sys
import os
from fundamentals import tools, times
import khufu


class login_form():

    """
    *The worker class for the login_form module*

    **Key Arguments:**
        - ``log`` -- logger
        - ``iconPath`` -- path to webapp icon
        - ``message`` -- message to display (warning)
    """

    def __init__(
        self,
        log,
        iconPath,
        message
    ):
        self.log = log
        log.debug("instansiating a new 'login_form' object")
        self.iconPath = iconPath
        self.message = message

        # xt-self-arg-tmpx

        # BUILD IMAGE WITH ICON PATH
        self.icon = khufu.image(
            src=iconPath,  # [ industrial | gray | social ]
            href=False,
            display="circle",  # [ rounded | circle | polaroid | False ]
            pull=False
        )

        return None

    def close(self):
        del self
        return None

    def get(self):
        """
        *get the login_form object*

        **Return:**
            - ``formContent`` -- the content of the login form
        """
        self.log.debug('starting the ``get`` method')

        formContent = self._setup_form()

        self.log.debug('completed the ``get`` method')
        return formContent

    def _setup_form(
            self):
        """
        *setup loging form*

        **Return:**
            - ``formContent`` -- content of the login form
        """
        self.log.debug('starting the ``_setup_form`` method')

        # username input
        username = khufu.formInput(
            ttype='text',
            placeholder='username',
            span=12,
            htmlId="login",
            required=True
        )
        username = khufu.controlRow(
            inputList=[username, ]
        )
        username = khufu.horizontalFormControlGroup(
            content=username,
            validationLevel=False
        )

        # password input
        password = khufu.formInput(
            ttype='password',
            placeholder='password',
            span=12,
            htmlId="password",
            required=True
        )
        password = khufu.controlRow(
            inputList=[password, ]
        )
        password = khufu.horizontalFormControlGroup(
            content=password,
            validationLevel=False
        )

        submit = khufu.button(
            buttonText='login',
            buttonStyle='info',
            buttonSize='default',  # [ large | default | small | mini ]
            htmlId="form.submitted",
            submit=True
        )
        submit = khufu.horizontalFormControlGroup(
            content=submit,
            validationLevel=False
        )

        # add a warning notification
        if len(self.message):
            self.message = khufu.alert(
                alertText=self.message,
                alertHeading="WARNING: ",
                extraPadding=False,
                alertLevel='error'
            )
            self.message = khufu.horizontalFormControlGroup(
                content=self.message,
                validationLevel=False
            )

        formContent = khufu.form(
            content=self.icon + username + password + submit + self.message,
            formType='inline',
            postToScript=""
        )

        self.log.debug('completed the ``_setup_form`` method')
        return formContent

    # xt-class-method
