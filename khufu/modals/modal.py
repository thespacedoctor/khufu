#!/usr/bin/env python
# encoding: utf-8
"""
modal.py
========
:Summary:
    Modal

:Author:
    David Young

:Date Created:
    July 1, 2014

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
from dryxPython import commonutils as dcu


###################################################################
# PUBLIC FUNCTIONS                                                #
###################################################################
# LAST MODIFIED : October 9, 2013
# CREATED : October 9, 2013
# AUTHOR : DRYX
def modal(
    modalHeaderContent="",
    modalBodyContent="",
    modalFooterContent="",
    htmlId=False,
    centerContent=False,
    htmlClass=False
):
    """generate a modal to by generated with a js event

    **Key Arguments:**
      - ``modalHeaderContent`` -- the heading for the modal
      - ``modalBodyContent`` -- the content (form or text)
      - ``modalFooterContent`` -- the foot (usually buttons)
      - ``htmlId`` -- id for button to hook onto with href
      - ``centerContent`` - center the content in the form?
      - ``htmlClass`` - htmlClass for the form

    **Return:**
        - ``modal`` -- the modal

    **Todo**
    """
    if htmlClass is False:
        htmlClass = ""

    if htmlId is False:
        htmlId = ""
    else:
        htmlId = """id="%(htmlId)s" """ % locals()
    if centerContent is False:
        centerContent = ""
    else:
        centerContent = "center-content"

    ## VARIABLES ##
    modal = """<div class="modal hide fade %(htmlClass)s" %(htmlId)s>
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h3>%(modalHeaderContent)s</h3>
      </div>
      <div class="modal-body %(centerContent)s">
        %(modalBodyContent)s
      </div>
      <div class="modal-footer">
        %(modalFooterContent)s
      </div>
    </div>""" % locals()

    return modal

if __name__ == '__main__':
    main()
