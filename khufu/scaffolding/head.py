# encoding: utf-8
from . import *


def head(
    relativeUrlBase=False,
    mainCssFilePath="main.css",
    pageTitle="",
    extras="",
    faviconLocation=False,
    assetsDirectory=False
):
    """ *Generate an html head element for your webpage*

    **Key Arguments:**
        ``relativeUrlBase`` -- relative base url for js, css, image folders
        ``pageTitle`` -- well, the page title!
        ``mainCssFilePath`` -- css file path
        ``extras`` -- any extra info to be included in the ``head`` element
        ``faviconLocation`` -- path to faviconLocation if not in document root

    **Return:**
        - ``head`` -- the head """

    if not relativeUrlBase:
        relativeUrlBase = ""

    cssLink = """
        <link rel="stylesheet" href="%(mainCssFilePath)s" type="text/css" />
    """ % locals()

    if faviconLocation is not False:
        faviconLocation = """
            <link rel="shortcut icon" href="%(faviconLocation)s" />
        """ % locals()
    else:
        faviconLocation = ""

    head = """
    <!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
    <!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
    <!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
    <!--[if gt IE 8]><!--> <html class="no-js"> <!--<![endif]-->
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <title>%(pageTitle)s</title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        %(cssLink)s
        %(extras)s
        %(faviconLocation)s
    </head>
    """ % locals()

    return head
