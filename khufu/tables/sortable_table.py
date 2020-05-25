#!/usr/bin/env python
# encoding: utf-8
"""
*A sortable, customisable HTML table*

:Author:
    David Young
"""
from __future__ import division
from builtins import str
from builtins import object
from past.utils import old_div
from . import *
import sys
import os
import datetime
import math
import re
# from ..__init__ import *
from khufu.typography import *
from khufu.addons import *
from khufu.tables import *
from khufu.helpers import *
from fundamentals import times

class sortable_table(object):
    """
    *The worker class for the sortable_table module*

    **Key Arguments**

    - ``dbConn`` -- mysql database connection
    - ``log`` -- logger
    - ``currentPageUrl`` -- the baseurl for the webpage
    - ``columnsToDisplay`` -- a list of column objects for the table
    - ``defaultSort`` -- the column to sort on by default
    - ``tableRowsDictionary`` -- dictionary of column names and values (e.g. a mysql query result)
    
    """

    def __init__(
            self,
            log,
            dbConn=False,
            currentPageUrl="",
            columnsToDisplay=[],
            defaultSort=False,
            tableRowsDictionary={}
    ):
        self.log = log
        self.dbConn = dbConn
        self.currentPageUrl = currentPageUrl
        self.columnsToDisplay = columnsToDisplay
        self.defaultSort = defaultSort
        self.tableRowsDictionary = tableRowsDictionary
        # xt-self-arg-tmpx

        # VARIABLE DATA ATRRIBUTES
        self.colors = ["green", "blue", "red",  "yellow",
                       "orange", "violet", "magenta", "cyan", ]
        self.modifyDisplayNameDict = {}
        self.modifySortByDict = {}
        self.modifyColumnWidths = []
        self.headerPopoverText = "click to sort"
        self.searchKeyAndColumn = False
        self.columnsToHide = []
        self.columnWidth = int(math.floor(old_div(100, len(self.columnsToDisplay))))
        self.extraColumnWidth = 100 - \
            self.columnWidth * len(self.columnsToDisplay)

        # DETERMINE HOW TABLE IS TO BE SORTED FROM URL
        thisSort = re.search(
            r'sortBy=(\w+)&',
            self.currentPageUrl,
            flags=0  # re.S
        )
        if thisSort:
            thisSort = thisSort.group(1)
        elif self.defaultSort:
            thisSort = self.defaultSort
        else:
            thisSort = False

        thisSortDesc = re.search(
            r'sortDesc=(\w+)&?',
            self.currentPageUrl,
            flags=0  # re.S
        )
        if thisSortDesc:
            thisSortDesc = thisSortDesc.group(1)
        else:
            thisSortDesc = "False"

        arrow = ""
        if "true" in thisSortDesc.lower():
            arrow = coloredText(
                text="""&nbsp&nbsp<i class="icon-arrow-up4"></i>""" % locals(),
                color="red",
            )
        else:
            arrow = coloredText(
                text="""&nbsp&nbsp<i class="icon-arrow-down4"></i>""",
                color="red",
            )
        self.thisSort = thisSort
        self.thisSortDesc = thisSortDesc
        self.arrow = arrow

        # REMOVE SORT AND SORTDESC FROM URL TO GENERAL A BASEURL FOR HEADER
        # SORTING
        reSort = re.compile(r'sortBy=\w+&?')
        reDesc = re.compile(r'sortDesc=\w+&?')
        self.baseUrl = reSort.sub("", self.currentPageUrl)
        self.baseUrl = reDesc.sub("", self.baseUrl)
        thisUrl = self.baseUrl
        if thisUrl[-3:] == ".py":
            thisUrl = "%(thisUrl)s?" % locals()
        elif "?" not in thisUrl:
            thisUrl = "%(thisUrl)s?" % locals()
        elif thisUrl[-1:] not in ["?", "&"]:
            thisUrl = "%(thisUrl)s&" % locals()
        self.baseUrl = thisUrl

        return None

    def close(self):
        del self
        return None

    def get(self):
        """
        *get the sortable_table object*

        **Return**

        - ``sortable_table``
        
        """

        tableHead = self.get_table_head()
        tbody = self.get_table_body()

        sortable_table = table(
            caption='',
            thead=tableHead,
            tbody=tbody,
            striped=True,
            bordered=False,
            hover=True,
            condensed=True,
        )

        return sortable_table

    def get_table_head(
            self):
        """
        *get table head*

        **Return**

        - ``tableHead`` -- the table head
        
        """
        tableHead = ""

        # BUILD THE TABLE HEADER
        _popover = popover(
            tooltip=True,
            placement="bottom",  # [ top | bottom | left | right ]
            trigger="hover",  # [ False | click | hover | focus | manual ]
            title=self.headerPopoverText,
            content=False,
            delay=600
        )

        colorIndex = 0
        columnIndex = 0

        for i, c in enumerate(self.columnsToDisplay):
            # build sort url
            direction = "False"
            if c in list(self.modifySortByDict.keys()):
                columnSortByAlias = self.modifySortByDict[c]
            else:
                columnSortByAlias = c

            if not columnSortByAlias:
                newSortUrl = False
                thisPopover = False
                thisArrow = ""
            else:
                thisPopover = _popover
                if self.thisSort == columnSortByAlias and self.thisSortDesc == "False":
                    direction = "True"
                thisUrl = self.baseUrl
                newSortUrl = """%(thisUrl)ssortBy=%(columnSortByAlias)s&sortDesc=%(direction)s""" % locals(
                )

                thisArrow = ""
                if self.thisSort and (columnSortByAlias.lower() == self.thisSort.lower()):
                    thisArrow = self.arrow

            # add text color and change display names if necessary
            if c in list(self.modifyDisplayNameDict.keys()):
                thisText = self.modifyDisplayNameDict[c]
            else:
                thisText = c
            self.modifyDisplayNameDict[c] = coloredText(
                text=thisText + thisArrow,
                color=self.colors[colorIndex],
                size=False,  # 1-10
                pull=False,  # "left" | "right"
            )
            if colorIndex < len(self.colors) - 1:
                colorIndex += 1
            else:
                colorIndex = 0

            if c not in self.columnsToHide:
                if len(self.modifyColumnWidths) == len(self.columnsToDisplay) - len(self.columnsToHide):
                    columnWidth = self.modifyColumnWidths[columnIndex]
                elif columnIndex < self.extraColumnWidth:
                    columnWidth = self.columnWidth + 1
                else:
                    columnWidth = self.columnWidth
                columnIndex += 1
                cell = th(
                    content=self.modifyDisplayNameDict[c],
                    color=False,
                    href=newSortUrl,
                    popover=thisPopover,
                    columnWidth=columnWidth
                )
                tableHead = "%(tableHead)s %(cell)s" % locals()

        tableHead = tr(
            cellContent=tableHead,
            color=False,
        )
        tableHead = thead(
            trContent=tableHead
        )
        return tableHead

    def get_table_body(
            self):
        """
        *get table body*

        **Return**

        - ``tableBody``
        
        """
        theseTickets = ""

        # BUILD THE TABLE BODY
        for obj in self.tableRowsDictionary:

            if self.searchKeyAndColumn:
                regex = re.compile(r'^(.*?)\?.*')
                href = regex.sub("\g<1>", self.baseUrl, count=1)
                href = href.replace("?", "")
                href = href + "\\" + \
                    self.searchKeyAndColumn[0] + "=" + \
                    obj[self.searchKeyAndColumn[1]]
            else:
                href = False

            tableRow = ""
            colorIndex = 0

            for i, c in enumerate(self.columnsToDisplay):

                if (isinstance(obj[c], ("".__class__, u"".__class__)) or isinstance(obj[c], str)) and "." not in obj[c]:
                    try:
                        obj[c] = int(obj[c])
                    except:
                        pass

                if not isinstance(obj[c], int):
                    try:
                        obj[c] = float(obj[c])
                    except:
                        pass

                if c.lower() in ["radeg", "decdeg"]:
                    obj[c] = "%6.3f" % obj[c]
                elif (isinstance(obj[c], float) or isinstance(obj[c], int)) and obj[c]:
                    obj[c] = "%6.2f" % obj[c]
                elif obj[c] == 0:
                    pass
                elif not obj[c] or ((isinstance(obj[c], ("".__class__, u"".__class__)) or isinstance(obj[c], str)) and ("unkn" in obj[c].lower())):
                    obj[c] = ""
                elif isinstance(obj[c], datetime.datetime):
                    # obj[c] = "boom"

                    relativeDate = times.datetime_relative_to_now(obj[c])
                    thisDate = str(obj[c])[:10]
                    thisDate = coloredText(
                        text="(%(thisDate)s)" % locals(),
                        color="grey",
                        size=2,
                    )
                    thisDate = hide_from_device(
                        content=thisDate,
                        onPhone=False,
                        onTablet=False,
                        onDesktop=True
                    )
                    obj[c] = "%(relativeDate)s %(thisDate)s" % locals()

                obj[c] = coloredText(
                    text=obj[c],
                    color=self.colors[colorIndex],
                )
                if colorIndex < len(self.colors) - 1:
                    colorIndex += 1
                else:
                    colorIndex = 0

                if c not in self.columnsToHide:
                    cell = td(
                        content=obj[c],
                    )
                    tableRow = "%(tableRow)s %(cell)s" % locals()

            tableRow = tr(
                cellContent=tableRow,
                color=False,
                href=href,
                popover=False,
            )
            theseTickets = "%(theseTickets)s%(tableRow)s" % locals()

        tableBody = tbody(
            trContent=theseTickets
        )
        return tableBody

    # xt-class-method
