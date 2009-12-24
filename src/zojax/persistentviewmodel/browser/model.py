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
from zope.proxy import removeAllProxies
from zope.component import getMultiAdapter
from zope.traversing.browser import absoluteURL

from z3c.form.interfaces import IFieldWidget

from zojax.layoutform import Fields, PageletEditSubForm
from zojax.wizard.button import WizardButton
from zojax.content.forms.form import AddForm
from zojax.content.type.interfaces import IContentView
from zojax.content.type.interfaces import IContentViewView
from zojax.persistentviewmodel.interfaces import _, IPersistentViewModel


def customWidget(field, request):
    widget = getMultiAdapter((field, request), IFieldWidget)

    widget.rows = 30
    widget.style = u'width: 98%; font-family: monospace; font-size: 130%'

    return widget


class AddViewModelForm(AddForm):

    fields = Fields(IPersistentViewModel)
    fields['source'].widgetFactory = customWidget


class EditViewModelForm(PageletEditSubForm):

    fields = Fields(IPersistentViewModel).omit('title', 'description')
    fields['source'].widgetFactory = customWidget

    def update(self):
        super(EditViewModelForm, self).update()

        if self.context.errors:
            IStatusMessage(self.request).add(self.context.errors[1], 'error')


class ViewModel(object):

    def __init__(self, context, request):
        super(ViewModel, self).__init__(context.context, request)

        self.model = context

        if context.contentView:
            interface.directlyProvides(self, IContentView)

    def render(self):
        return self.model.renderView()


class ModelViewView(object):
    interface.implements(IContentViewView)
    component.adapts(IPersistentViewModel, interface.Interface)

    name = u'context.html'

    def __init__(self, image, request):
        pass


# back action
class BackButton(WizardButton):

    def actionHandler(self):
        return self.wizard.redirect('%s/'%absoluteURL(
                self.wizard.__parent__.__parent__, self.request))


backButton = BackButton(title = _(u'Back'), weight = 502)
