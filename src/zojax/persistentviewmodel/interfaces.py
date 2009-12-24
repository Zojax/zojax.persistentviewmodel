##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""

$Id$
"""
from zope import schema, interface
from zope.i18nmessageid import MessageFactory
from zojax.content.model.interfaces import IViewModel

_ = MessageFactory('zojax.persistentviewmodel')


class IPersistentViewModel(IViewModel):
    """ persistent view model """

    title = schema.TextLine(
        title = _(u'Title'),
        description = _(u'View model title'),
        default = u'',
        missing_value = u'',
        required = False)

    description = schema.Text(
        title = _(u'Description'),
        description = _(u'View model description'),
        default = u'',
        missing_value = u'',
        required = False)

    contentView = schema.Bool(
        title = _(u'Content view'),
        description = _(u'View model is view content.'),
        default = False,
        required = False)

    contentType = schema.List(
        title = _(u'Content type'),
        description = _(u''),
        value_type = schema.Choice(
            vocabulary='zojax.contentext.persistentview.types'),
        default = ['__all__'],
        required = True)

    def getSource():
        """Get the source of the page element."""

    def setSource(text, content_type='text/html'):
        """Save the source of the page element.

        'text' must be Unicode.
        """

    source = schema.SourceText(
        title=_("Source"),
        description=_("The source of the view model."),
        required=True)


class IViewModelsConfiglet(interface.Interface):
    """ configlet """
