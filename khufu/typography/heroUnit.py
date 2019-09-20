# encoding: utf-8
from . import *


def heroUnit(
        headline="",
        tagline="",
        buttonStyle="primary",
        buttonText="",
        buttonHref="#"
):
    """
    *Generate a heroUnit - TBS style*

    **Key Arguments:**
        - ``headline`` -- the headline text
        - ``tagline`` -- the tagline text for below the headline
        - ``buttonStyle`` -- the style of the button to be used
        - ``buttonText`` -- the text for the button
        - ``buttonHref`` -- the anchor link for the button

    **Return:**
        - ``heroUnit`` -- the heroUnit
    """
    heroUnit = """
        <div class="hero-unit" id="  ">
            <h1>%(headline)s</h1>
            <p>%(tagline)s</p>
            <p>
                <a href="%(buttonHref)s" class="btn btn-%(buttonStyle)s btn-large">
                  %(buttonText)s
                </a>
            </p>
        </div>""" % locals()

    return heroUnit
