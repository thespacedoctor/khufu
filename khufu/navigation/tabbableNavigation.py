# encoding: utf-8
from . import *
import khufu


def tabbableNavigation(
        contentDictionary={},  # { name : content }
        fadeIn=True,
        direction='top',
        htmlClass=False,
        htmlId=False,
        uniqueNavigationId=False,
        contentCount={}
):
    """ Generate a tabbable Navigation

    **Key Arguments:**
        - ``contentDictionary`` -- the content dictionary { name : content }
        - ``fadeIn`` -- make tabs fade in
        - ``direction`` -- the position of the tabs [ above | below | left | right ]
        - ``uniqueNavigationId`` -- a unique id for this navigation block if more than one on page

    **Return:**
        - ``tabbableNavigation`` -- the tabbableNavigation """

    if fadeIn is True:
        fadeIn = 'fade'
    else:
        fadeIn = ''
    titleList = ''
    contentList = ''
    count = 0

    # turn contentCounts into badges
    for i in contentDictionary.keys():
        if i in contentCount.keys():
            contentCount[i] = khufu.badge(
                text=str(contentCount[i]),
                level='inverse'
            )
        else:
            contentCount[i] = ""

    if htmlClass is False:
        htmlClass = ""

    if htmlId is False:
        htmlId = ""
    else:
        htmlId = """id="%(htmlId)s" """ % locals()

    if uniqueNavigationId is False:
        uniqueNavigationId = ""
    elif isinstance(uniqueNavigationId, int):
        uniqueNavigationId = """id%(uniqueNavigationId)s""" % locals()

    for k, v in contentDictionary.iteritems():
        badge = contentCount[k]
        if count == 0:
            titleList = """%(titleList)s<li class="active"><a href="#tab%(uniqueNavigationId)s%(count)s" data-toggle="tab">%(k)s %(badge)s</a></li>""" % locals(
            )
            contentList = \
                """%(contentList)s
                <div class="tab-pane active %(fadeIn)s" id="tab%(uniqueNavigationId)s%(count)s">
                    <p>%(v)s</p>
                </div>""" \
                % locals()
        else:
            titleList = """%(titleList)s<li><a href="#tab%(uniqueNavigationId)s%(count)s" data-toggle="tab">%(k)s %(badge)s</a></li>""" % locals(
            )
            contentList = \
                """%(contentList)s
                <div class="tab-pane %(fadeIn)s" id="tab%(uniqueNavigationId)s%(count)s">
                    <p>%(v)s</p>
                </div>""" \
                % locals()
        count += 1
    tabbableNavigation = \
        """
        <div class="tabbable %(htmlClass)s" %(htmlId)s>
            <ul class="nav nav-tabs">
                %(titleList)s
            </ul>
            <div class="tab-content">
                %(contentList)s
            </div>
        </div>""" \
        % locals()
    if direction != 'top':
        tabbableNavigation = \
            """
            <div class="tabbable tabs-%(direction)s %(htmlClass)s" %(htmlId)s>
                <div class="tab-content">
                    %(contentList)s
                </div>
                <ul class="nav nav-tabs">
                    %(titleList)s
                </ul>
            </div>""" \
            % locals()
    return tabbableNavigation
