# encoding: utf-8
from . import *


def tbody(
        trContent=""):
    """
    *Generate a table body - TBS style*

    **Key Arguments:**
        - ``trContent`` -- the table row content

    **Return:**
        - ``tbody`` -- the table body
    """

    if isinstance(trContent, list):
        new = ""
        for c in trContent:
            new += c
        trContent = new

    tbody = """<tbody class="">%(trContent)s</tbody>""" % locals()

    return tbody
