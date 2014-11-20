# encoding: utf-8
from . import *

# LAST MODIFIED : May 22, 2014
# CREATED : May 22, 2014
# AUTHOR : DRYX


def dropdownLinkList(
        linkDictionary={},
        title="dropdown",
        dropDirection="down"
):
    """dropdownLinkList

    **Key Arguments:**
        - ``log`` -- logger
        - ``linkDictionary`` -- { text : href }
        - ``title`` -- title for the dropdown
        - ``dropDirection`` -- up or down


    **Return:**
        - None

    **Todo**
        - @review: when complete, clean dropdownLinkList function
        - @review: when complete add logging
        - @review: when complete, decide whether to abstract function to another module
    """
    from . import *

    linkList = []
    for k, v in linkDictionary.iteritems():
        link = a(
            content=k,
            href=v,
            tableIndex=False,
            triggerStyle=False,  # [ False | "dropdown" | "tab" | "modal" ],
            htmlClass=False,
            postInBackground=False,
            openInNewTab=True,
            popover=False,
        )
        link = li(
            content=link,  # if a subMenu for dropdown this should be <ul>
            span=False,  # [ False | 1-12 ]
            disabled=False,
            submenuTitle=False,
            divider=False,
            navStyle=False,  # [ active | header ]
            navDropDown=False,
            pager=False,  # [ False | "previous" | "next" ]
        )
        linkList.append(link)
    thisDropdown = dropdown(
        buttonSize='small',
        buttonColor='default',  # [ default | sucess | error | warning | info ]
        linkNotButton=True,
        menuTitle=title,
        splitButton=False,
        linkList=linkList,
        separatedLinkList=False,
        pull="right",
        # use javascript to explode contained links
        htmlClass=False,
        direction=dropDirection,  # [ down | up ]
        onPhone=True,
        onTablet=True,
        onDesktop=True
    )

    return thisDropdown