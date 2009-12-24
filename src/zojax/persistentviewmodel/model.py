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
from zope import interface, component
from zope.size import byteDisplay
from zope.size.interfaces import ISized
from zope.component import getMultiAdapter
from zope.app.pagetemplate.engine import TrustedAppPT
from zope.pagetemplate.pagetemplate import PageTemplate
from zope.app.container.contained import Contained
from zope.app.container.interfaces import IObjectMovedEvent
from zope.publisher.interfaces import NotFound

from zojax.content.type.item import PersistentItem
from zojax.content.type.interfaces import \
    IContent, IContentType, IContentView, IPortalType

from interfaces import IPersistentViewModel


class ViewModel(TrustedAppPT, PageTemplate, PersistentItem):
    interface.implements(IPersistentViewModel)

    expand = False
    errors = ()
    elements = ()
    __schema__ = None

    @property
    def __title__(self):
        return self.title

    @property
    def __description__(self):
        return self.description

    def getSource(self, request=None):
        return self._text

    def setSource(self, text, content_type='text/html'):
        if not isinstance(text, unicode):
            raise TypeError("source text must be Unicode" , text)
        self.pt_edit(text, content_type)

        if self._v_errors:
            self.errors = self._v_errors
        else:
            self.errors = ()

    source = property(getSource, setSource, None,
                      """Source of the Page Element.""")

    def pt_getContext(self):
        namespace = super(ViewModel, self).pt_getContext()
        namespace['request'] = self.request
        namespace['context'] = self.context
        namespace['template'] = self
        namespace['views'] = ViewMapper(self.context, self.request)
        return namespace

    def isAvailable(self):
        ct = IContentType(self.context, None)
        if ct is None:
            return False

        if '__all__' in self.contentType:
            if IPortalType.providedBy(ct):
                return True
            else:
                return False
        elif ct.name in self.contentType:
            return True

        return False

    def __call__(self, context, request):
        self._p_activate()

        clone = BoundViewModel()  #self.__class__.__new__(self.__class__)
        clone.__dict__.update(self.__dict__)
        clone.__parent__ = context
        clone.context = context
        clone.request = request
        return clone

    def publishTraverse(self, request, name):
        view = component.queryMultiAdapter((self, request), name=name)
        if view is not None:
            return view

        raise NotFound(self, request, name)

    def browserDefault(self, request):
        return self, ('index.html',)


class BoundViewModel(ViewModel):

    def update(self):
        pass

    def renderView(self):
        return self.pt_render(self.pt_getContext())


class ViewMapper(object):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __getitem__(self, name):
        return getMultiAdapter((self.context, self.request), name=name)


@component.adapter(IPersistentViewModel, IObjectMovedEvent)
def viewModelMoved(element, event):
    sm = component.getSiteManager()

    if event.oldName is not None:
        sm.unregisterAdapter(
            element,
            (IContent, interface.Interface),
            IPersistentViewModel, event.oldName)

    if event.newName is not None:
        sm.registerAdapter(
            element,
            (IContent, interface.Interface),
            IPersistentViewModel, event.newName)


class Sized(object):
    interface.implements(ISized)
    component.adapts(IPersistentViewModel)

    def __init__(self, context):
        self.context = context

        self.size = len(context.title) + \
                    len(context.description) + \
                    len(context.source)

    def sizeForSorting(self):
        return "byte", self.size

    def sizeForDisplay(self):
        return byteDisplay(self.size)
