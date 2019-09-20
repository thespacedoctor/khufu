# !/usr/bin/env python
# encoding: utf-8
"""
*The modal form class*

:Author:
    David Young

:Date Created:
    July 1, 2014

"""
import sys
import os
import datetime
import numpy as np
import khufu
from khufu.forms import *
from khufu.scaffolding import *
from khufu.buttons import *
from . import modal


class modalForm():

    """
    *The worker class for the modalForm module*

    **Key Arguments:**
        - ``log`` -- logger
        - ``title`` -- title
        - ``postToScriptUrl`` -- postToScriptUrl
        - ``reloadToUrl`` -- reloadToUrl
        - ``formClassName`` -- give a class name to form (if required by CSS or JS)
    """

    def __init__(
        self,
        log,
        title,
        postToScriptUrl,
        reloadToUrl,
        formClassName=False
    ):
        self.log = log
        self.title = title
        self.postToScriptUrl = postToScriptUrl
        self.reloadToUrl = reloadToUrl
        self.formClass = formClassName
        # xt-self-arg-tmpx

        # VARIABLE DATA ATRRIBUTES
        self.formContent = u""
        self.randNum = int(np.random.rand() * 10000)
        self.hiddenParameterList = []
        # ADD REQUIRED ICON IF NEEDED
        self.requredIcon = khufu.coloredText(
            text="*",
            color="red",
            size=5,  # 1-10
            pull=False,  # "left" | "right",
            addBackgroundColor=False
        )
        self.submitButtonText = "submit"

        return None

    def close(self):
        del self
        return None

    def get(self):
        """
        *get the modalForm object*

        **Return:**
            - ``modalForm``
        """
        self.log.debug('starting the ``get`` method')

        randNum = self.randNum
        modalTrigger = "modalTrigger%(randNum)s" % locals()
        formId = "form%(randNum)s" % locals()

        self.set_hidden_parameters()

        modalForm = form(
            content=self.formContent,  # list of control groups
            # [ "inline" | "horizontal" | "search" | "navbar-form" | "navbar-search" ]
            formType='horizontal',
            navBarPull=False,  # [ false | right | left ],
            postToScript=self.postToScriptUrl,
            htmlId=formId,
            htmlClass=self.formClass,
            postInBackground=True,
            redirectUrl=self.reloadToUrl,
            span=12,
            offset=False
        )

        modalForm = grid_row(
            responsive=True,
            columns=modalForm,
            htmlId=False,
            htmlClass=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )

        # THE REQUIRED INPUT FOOTNOTE
        requredIcon = self.requredIcon
        requredAlert = '%(requredIcon)s required input &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp' % locals(
        )

        modalForm = modal(
            modalHeaderContent=self.title,
            modalBodyContent=modalForm,
            modalFooterContent=requredAlert +
            self.get_form_action_buttons(formId),
            htmlId=modalTrigger,
            centerContent=True
        )

        modalTrigger = "#%(modalTrigger)s" % locals()

        self.log.debug('completed the ``get`` method')
        return modalForm, modalTrigger

    def add_form_object(
            self,
            formObject,
            label="",
            hidden=False):
        """
        *add a form objec to the modal form*

        **Key Arguments:**
            - ``formObject`` -- the object to add to the form
            - ``label`` -- label to assign to the object
            - ``hidden`` -- is the form object hidden initially?
        """
        self.log.debug('starting the ``addFormObject`` method')

        randNum = self.randNum
        randId = "randId%(randNum)s" % locals()
        formObject = formObject.replace(
            "class=", """id="%(randId)s" class=""" % locals())

        if " required " in formObject:
            label = label + self.requredIcon

        thisControlRow = controlRow(
            inputList=[formObject, ]
        )
        thisContentLabel = horizontalFormControlLabel(
            labelText=label,
            forId=randId,
            location="left"
        )
        thisContentCG = horizontalFormControlGroup(
            content=thisContentLabel + thisControlRow,
            validationLevel=False
        )
        self.formContent = self.formContent + thisContentCG

        self.log.debug('completed the ``addFormObject`` method')
        return None

    def get_form_action_buttons(
            self,
            formId):
        """
        *get form action buttons*

        **Key Arguments:**
            - ``formId`` -- the HTML id of the form

        **Return:**
            - ``actionButtons`` -- the action buttos for the form (cancel, submit)
        """
        self.log.debug('starting the ``get_form_action_buttons`` method')

        cancel = button(
            buttonText='cancel',
            # [ default | primary | info | success | warning | danger | inverse | link ]
            buttonStyle='danger',
            buttonSize='small',  # [ large | default | small | mini ]
            htmlId=False,
            href=False,
            pull=False,  # right, left, center
            submit=False,
            block=False,
            disable=False,
            postInBackground=False,
            dataToggle=False,  # [ modal ]
            popover=False,
            close=True
        )

        submit = button(
            buttonText=self.submitButtonText,
            # [ default | primary | info | success | warning | danger | inverse | link ]
            buttonStyle='info',
            buttonSize='small',  # [ large | default | small | mini ]
            htmlId=False,
            href=False,
            pull=False,  # right, left, center
            submit=True,
            block=False,
            disable=False,
            postInBackground=False,
            dataToggle=False,  # [ modal ]
            popover=False,
            formId=formId,
            close=True
        )

        actionButtons = buttonGroup(
            buttonList=[cancel, submit],
            format='default'  # [ default | toolbar | vertical ]
        )

        self.log.debug('completed the ``get_form_action_buttons`` method')
        return actionButtons

    def add_hidden_parameter_value(
            self,
            key,
            value):
        """
        *add hidden parameter value to the form (to be submitted with the form but does not need user input)*

        **Key Arguments:**
            - ``key`` -- the key for the hidden value (will be appended to query string when form submitted)
            - ``value`` -- the value of the hidden parameter
        """
        self.log.debug('starting the ``add_hidden_parameter_value`` method')

        if isinstance(value, str):
            ttype = "text"
        if isinstance(value, unicode):
            ttype = "text"
        elif isinstance(value, datetime.date):
            ttype = "datetime"
        else:
            ttype = "number"

        thisInput = formInput(
            # [ text | password | datetime | datetime-local | date | month | time | week | number | email | url | search | tel | color ]
            ttype=ttype,
            htmlId=key,
            hidden=True,
            defaultValue=value
        )
        self.hiddenParameterList.append(thisInput)

        self.log.debug('completed the ``add_hidden_parameter_value`` method')
        return None

    def set_hidden_parameters(
            self):
        """
        *get hidden parameters*
        """
        self.log.debug('starting the ``set_hidden_parameters`` method')

        thisControlRow = controlRow(
            inputList=self.hiddenParameterList
        )
        thisContentCG = horizontalFormControlGroup(
            content=thisControlRow,
            validationLevel=False,
            hidden=True
        )

        self.formContent = self.formContent + thisContentCG

        self.log.debug('completed the ``set_hidden_parameters`` method')
        return

    # xt-class-method
