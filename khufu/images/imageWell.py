#!/usr/bin/env python
# encoding: utf-8
"""
*Class to generate a well of images*

:Author:
    David Young

:Date Created:
    April 29, 2014
"""
import sys
import os
import math
from ..__init__ import *
from imagingModal import imagingModal


class imageWell():

    """
    *Framework for a bootstrap style well containing thumbnail images that can be clicked on to reveal a modal of more imformation*

    **Key Arguments:**
        - ``log`` -- logger
        - ``title`` -- Title of Image Well
        - ``description`` -- Description of the content of the image well
        - ``imageDisplay`` -- [ rounded | circle | polaroid | False ]
    """

    def __init__(
            self,
            log,
            title="Title of Image Well",
            description="Description of the content of the image well",
            imageDisplay="rounded"
    ):
        self.log = log
        self.description = description
        self.title = title
        self.description = description
        self.imageDisplay = imageDisplay
        self.imageColumns = []
        self.imageSpan = 2
        self.rowLength = 0

        return None

    def close(self):
        del self
        return None

    def get(self):
        """
        *get the image well*

        **Return:**
            - ``imageWellRow`` -- the html text
        """
        self.log.debug('starting the ``get`` method')

        ## VARIABLES ##
        numImages = len(self.imageColumns)
        colPerRow = int(math.floor(12 / self.imageSpan))
        numRows = int(math.ceil(float(numImages) / float(colPerRow)))

        # header text for the image well
        self.title = pageHeader(
            headline=self.title,
            tagline=self.description
        )

        # determine the number of rows from the number and span of the images
        # populate each of the rows and then append to ``theseRows``
        theseRows = ""
        for r in range(int(numRows)):
            startC = r * colPerRow
            endC = startC + colPerRow
            columns = " ".join(self.imageColumns[startC:endC])
            thisRow = grid_row(
                responsive=True,
                columns=columns,
                htmlId=False,
                htmlClass=False,
                onPhone=True,
                onTablet=True,
                onDesktop=True
            )
            theseRows = """%(theseRows)s %(thisRow)s""" % locals()

        # bunch all the image rows into one parent row
        content = grid_row(
            responsive=True,
            columns=theseRows,
            htmlId=False,
            htmlClass=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )

        # add header text and image rows to a well
        imageWell = well(
            wellText=self.title + content,
            wellSize='large',  # [ "default" | "large" | "small" ]
            htmlId=False,
            htmlClass="imagewell"
        )

        # wrapper the well in a parent row
        imageWellRow = grid_row(
            responsive=True,
            columns=imageWell,
            htmlId=False,
            htmlClass="imagewell-row",
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )

        self.log.debug('completed the ``get`` method')
        return  """%(imageWellRow)s""" % locals()

    def appendImage(
            self,
            imagePath,
            imageTitle,
            modalHeaderContent="",
            modalFooterContent="",
            modalFooterButtons=[]):
        """
        *append an image to the image well*

        **Key Arguments:**
            - ``imagePath`` -- path to the image to add to the well
            - ``imageTitle`` -- text to tag the image with
            - ``modalHeaderContent`` -- the heading for the modal
            - ``modalFooterContent`` -- the footer (usually buttons)

        **Return:**
            - None
        """
        self.log.debug('starting the ``appendImage`` method')

        # PACKAGE THE IMAGE UP WITH A MODAL TO VIEW A LARGER VERSION WITH
        # DOWNLOAD OPTION
        thisImage = imagingModal(
            log=self.log,
            imagePath=imagePath,
            display=self.imageDisplay,
            modalHeaderContent=modalHeaderContent,
            modalFooterContent=modalFooterContent,
            modalFooterButtons=modalFooterButtons,
            stampWidth=180,
            modalImageWidth=800,)
        thisImage = thisImage.get()

        # COLOR THE TITLE TEXT AND MAKE IT THE CORRECT SIZE
        imageTitle = coloredText(
            text=imageTitle,
            color="lightgrey",
            size=3,  # 1-10
        )

        # POSITION THE TITLE TEXT CORRECTLY UNDER EACH IMAGE
        imageTitle = row_adjustable(
            span=12 - (self.imageSpan - 1),
            offset=self.imageSpan - 1,
            content=imageTitle,
            htmlId=False,
            htmlClass=False,
            onPhone=True,
            onTablet=True,
            onDesktop=True
        )

        # PACKAGE THE IMAGE AND TITLE, ADD TO PARENT COLUMN AND APPEND TO MASTER
        # IMAGE LIST
        content = "%(thisImage)s%(imageTitle)s" % locals()
        column = grid_column(
            span=self.imageSpan,  # 1-12
            offset=0,  # 1-12
            content=content,
        )
        self.imageColumns.append(column)

        self.log.debug('completed the ``appendImage`` method')
        return None

    # method-tmpx
