# !/usr/bin/env python
# encoding: utf-8
"""
modalForm.py
============
:Summary:
    The modal form class

:Author:
    David Young

:Date Created:
    July 1, 2014

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
import datetime
import numpy as np
import khufu
from docopt import docopt
from dryxPython import commonutils as dcu
from ..__init__ import *
from . import modal

###################################################################
# CLASSES                                                         #
###################################################################


class modalForm():

    """
    The worker class for the modalForm module

    **Key Arguments:**
        - ``log`` -- logger
        - ``title`` -- title
        - ``postToScriptUrl`` -- postToScriptUrl
        - ``reloadToUrl`` -- reloadToUrl

    **Todo**
        - @review: when complete, clean modalForm class
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract class to another module
    """
    # Initialisation

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

        # Variable Data Atrributes
        self.formContent = u""
        self.randNum = int(np.random.rand() * 10000)
        self.hiddenParameterList = []
        # add required icon if needed
        self.requredIcon = khufu.coloredText(
            text="*",
            color="red",
            size=5,  # 1-10
            pull=False,  # "left" | "right",
            addBackgroundColor=False
        )
        self.submitButtonText = "submit"

        # 3. @flagged: what variable attrributes need overriden in any baseclass(es) used
        # Override Variable Data Atrributes

        # Initial Actions

        return None

    def close(self):
        del self
        return None

    # 4. @flagged: what actions does each object have to be able to perform? Add them here
    # Method Attributes
    def get(self):
        """get the modalForm object

        **Return:**
            - ``modalForm``

        **Todo**
            - @review: when complete, clean get method
            - @review: when complete add logging
        """
        self.log.info('starting the ``get`` method')

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

        # The required input footnote
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

        self.log.info('completed the ``get`` method')
        return modalForm, modalTrigger

    def add_form_object(
            self,
            formObject,
            label="",
            hidden=False):
        """add a form objec to the modal form

        **Key Arguments:**
            # -

        **Return:**
            - None

        **Todo**
            - @review: when complete, clean addFormObject method
            - @review: when complete add logging
        """
        self.log.info('starting the ``addFormObject`` method')

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

        self.log.info('completed the ``addFormObject`` method')
        return None

    # use the tab-trigger below for new method
    def get_form_action_buttons(
            self,
            formId):
        """get form action buttons

        **Key Arguments:**
            # -

        **Return:**
            - None

        **Todo**
            - @review: when complete, clean get_form_action_buttons method
            - @review: when complete add logging
        """
        self.log.info('starting the ``get_form_action_buttons`` method')

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

        self.log.info('completed the ``get_form_action_buttons`` method')
        return actionButtons

    # use the tab-trigger below for new method
    def add_hidden_parameter_value(
            self,
            key,
            value):
        """add hidden parameter value to the form (to be submitted with the form but does not need user input)

        **Key Arguments:**
            # -

        **Return:**
            - None

        **Todo**
            - @review: when complete, clean add_hidden_parameter_value method
            - @review: when complete add logging
        """
        self.log.info('starting the ``add_hidden_parameter_value`` method')

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

        self.log.info('completed the ``add_hidden_parameter_value`` method')
        return None

    # use the tab-trigger below for new method
    def set_hidden_parameters(
            self):
        """get hidden parameters

        **Key Arguments:**
            # -

        **Return:**
            - None

        **Todo**
            - @review: when complete, clean set_hidden_parameters method
            - @review: when complete add logging
        """
        self.log.info('starting the ``set_hidden_parameters`` method')

        thisControlRow = controlRow(
            inputList=self.hiddenParameterList
        )
        thisContentCG = horizontalFormControlGroup(
            content=thisControlRow,
            validationLevel=False,
            hidden=True
        )

        self.formContent = self.formContent + thisContentCG

        self.log.info('completed the ``set_hidden_parameters`` method')
        return

    # use the tab-trigger below for new method
    # xt-class-method


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

############################################
# CODE TO BE DEPECIATED                    #
############################################

if __name__ == '__main__':
    main()

###################################################################
# TEMPLATE FUNCTIONS                                              #
###################################################################
