# !/usr/bin/env python
# encoding: utf-8
"""
*An image and modal -- click on the image to present the modal of the larger image with download options*

:Author:
    David Young

:Date Created:
    April 30, 2014
"""
import sys
import os
import numpy as np
from ..__init__ import *
from .. import modals
from image import image


class imagingModal():

    """
    *An image and modal -- click on the image to present the modal of the larger image with download options*

    **Key Arguments:**
        - ``dbConn`` -- mysql database connection
        - ``log`` -- logger
        - ``display`` -- [ rounded | circle | polaroid | False ]
        - ``imagePath`` -- path to the image to be displayed
        - ``modalHeaderContent`` -- the heading for the modal
        - ``modalFooterContent`` -- the footer (usually buttons)
        - ``stampWidth`` -- 180
        - ``modalImageWidth`` -- 400
        - ``downloadLink`` -- False
    """

    def __init__(
            self,
            log,
            dbConn=False,
            imagePath=False,
            display=False,
            modalHeaderContent="",
            modalFooterContent="",
            modalFooterButtons=[],
            stampWidth=180,
            modalImageWidth=400,
            downloadLink=False
    ):
        self.log = log
        self.dbConn = dbConn
        self.imagePath = imagePath
        self.display = display
        self.modalHeaderContent = modalHeaderContent
        self.modalFooterContent = modalFooterContent
        self.randomNum = np.random.randint(300000000)
        self.stampWidth = stampWidth
        self.modalImageWidth = modalImageWidth
        self.downloadLink = downloadLink
        self.modalFooterButtons = modalFooterButtons
        # x-self-arg-tmpx
        return None

    def close(self):
        del self
        return None

    def get(self):
        """
        *get the object*

        **Return:**
            - ``imageModal``
        """
        self.log.debug('starting the ``get`` method')

        # CREATE IMAGING MODAL AND ASSOCIATED IMAGE AND RETURN THEM
        thisImage = self._create_image(width=self.stampWidth)
        thisModal = self._create_modal()

        self.log.debug('completed the ``get arse`` method')
        return thisImage + thisModal

    def _create_image(
            self,
            width=False):
        """
        *create the html for the image

         - ``width`` -- image width*

        **Return:**
            - ``thisImage`` -- the image created
        """
        self.log.debug('starting the ``create_image`` method')

        # ADD PLACEHOLDER AS DEFAULT IMAGE
        if not self.imagePath:
            self.imagePath = 'holder.js/200x200/auto/industrial/text:placeholder'

        # CREATE HTML CODE FOR THE IMAGE
        thisImage = image(
            src=self.imagePath,  # [ industrial | gray | social ]
            href=False,
            display=self.display,  # [ rounded | circle | polaroid | False ]
            pull=False,  # [ "left" | "right" | "center" | False ]
            htmlClass=False,
            width=width,
            thumbnail=True
        )

        # LINK THE IMAGE TO THE ASSOCIATED MODAL WITH A RANDOM NUMBER TAG
        randNum = self.randomNum
        thisImage = a(
            content=thisImage,
            href="#modal%(randNum)s" % locals(),
            tableIndex=False,
            triggerStyle="modal",  # [ False | "dropdown" | "tab" ]
            htmlClass=False,
            postInBackground=False,
        )

        self.log.debug('completed the ``create_image`` method')
        return thisImage

    def _create_modal(
            self):
        """
        *create modal*

        **Return:**
            - ``imageModal`` -- the image modal
        """
        self.log.debug('starting the ``create_modal`` method')

        # GRAB THE ASSOCIATED IMAGE AND PLACE IN A WRAPPER ROW
        thisImage = self._create_image(width=self.modalImageWidth)
        thisImage = row_adjustable(
            span=10,
            offset=1,
            content=thisImage,
            htmlId=False,
            htmlClass=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )

        # GENERATE THE DOWNLOAD BUTTON FOR THE MODAL FOOTER
        fileUrl = self.imagePath

        thisPopover = popover(
            tooltip=True,
            placement="bottom",  # [ top | bottom | left | right ]
            trigger="hover",  # [ False | click | hover | focus | manual ]
            title="download image",
            content=False,
            delay=20
        )

        if self.downloadLink:
            downloadLink = self.downloadLink
            downloadFileButton = button(
                buttonText="""<i class="icon-file-pdf"></i>""",
                # [ default | primary | info | success | warning | danger | inverse | link ]
                buttonStyle='primary',
                buttonSize='small',  # [ large | default | small | mini ]
                htmlId=False,
                href=downloadLink,
                pull=False,  # right, left, center
                submit=False,
                block=False,
                disable=False,
                dataToggle=False,  # [ modal ]
                popover=thisPopover
            )
        else:
            downloadFileButton = ""

        buttonList = [downloadFileButton]
        buttonList.extend(self.modalFooterButtons)

        thisButtonGroup = buttonGroup(
            buttonList=buttonList,
            format='default'  # [ default | toolbar | vertical ]
        )

        # CREATE THE MODAL WITH THE CORRECT TRIGGER TAG
        randNum = self.randomNum
        imageModal = modals.modal(
            modalHeaderContent=self.modalHeaderContent,
            modalBodyContent=thisImage,
            modalFooterContent=self.modalFooterContent + thisButtonGroup,
            htmlId="modal%(randNum)s" % locals(),
            centerContent=True,
            htmlClass=False
        )

        self.log.debug('completed the ``create_modal`` method')
        return imageModal

    # method-tmpx
