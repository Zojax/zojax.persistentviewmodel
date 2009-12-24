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
from zope import interface
from zope.component import getUtilitiesFor
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary
from zojax.content.type.interfaces import IPortalType

from interfaces import _


class PortalTypes(object):
    interface.implements(IVocabularyFactory)

    def __call__(self, context):
        types = []

        for name, ptype in getUtilitiesFor(IPortalType):
            types.append((ptype.title, ptype.name))

        types.sort()
        return SimpleVocabulary(
            [SimpleTerm('__all__', '__all__', _('All types'))] +
            [SimpleTerm(name, name, title) for title, name in types])
