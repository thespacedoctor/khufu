# encoding: utf-8
from khufu.scaffolding import _container


def body(
        navBar=False,
        content="",
        htmlId="",
        extraAttr="",
        relativeUrlBase=False,
        responsive=True,
        googleAnalyticsCode=False,
        jsFilePath="main.js"
):
    """
    *Generate an HTML body*

    **Key Arguments:**
        - ``navBar`` -- the top navigation bar
        - ``htmlId`` -- *id* attribute of the body
        - ``content`` -- body content built from smaller HTML code blocks
        - ``extraAttr`` -- an extra attributes to be added to the body definition
        - ``relativeUrlBase`` -- how to get back to the document root
        - ``responsive`` -- should the webpage be responsive to screen-size?
        - ``googleAnalyticsCode`` -- google analytics code for the website
        - ``jsFilePath`` -- the name of the main javascript file

    **Return:**
        - ``body`` -- the body
    """
    if not navBar:
        navBar = ""

    if googleAnalyticsCode:
        googleAnalyticsCode = """
        <!-- Google Analytics -->
        <script>
            var _gaq=[['_setAccount','%(googleAnalyticsCode)s'],['_trackPageview']];
            (function(d,t){var g=d.createElement(t),s=d.getElementsByTagName(t)[0];
            g.src=('https:'==location.protocol?'//ssl':'//www')+'.google-analytics.com/ga.js';
            s.parentNode.insertBefore(g,s)}(document,'script'));
        </script>
        """ % locals()
    else:
        googleAnalyticsCode = ""

    if relativeUrlBase is False:
        relativeUrlBase = ""

    container = _container(
        responsive=responsive,
        content=content,
        htmlId=False,
        htmlClass=False,
        onPhone=True,
        onTablet=True,
        onDesktop=True,
    )

    body = \
        """
      <body id="%(htmlId)s" %(extraAttr)s>
      <!--[if lt IE 7]>
        <p class="chromeframe">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> or <a href="http://www.google.com/chromeframe/?redirect=true">activate Google Chrome Frame</a> to improve your experience.</p>
      <![endif]-->
        %(navBar)s
        %(container)s
      <script src="%(jsFilePath)s"></script>
      %(googleAnalyticsCode)s
      </body><!-- /#%(htmlId)s-->
      """ \
        % locals()

    return body
