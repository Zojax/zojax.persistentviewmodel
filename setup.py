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
""" Setup for zojax.persistentviewmodel package

$Id$
"""
import sys, os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version='1.3.6'


setup(name = 'zojax.persistentviewmodel',
      version = version,
      author = 'Nikolay Kim',
      author_email = 'fafhrd91@gmail.com',
      description = "Persistent View Model",
      long_description = (
        'Detailed Documentation\n' +
        '======================\n'
        + '\n\n' +
        read('CHANGES.txt')
        ),
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Zope3'],
      url='http://zojax.net/',
      license='ZPL 2.1',
      packages=find_packages('src'),
      package_dir = {'':'src'},
      namespace_packages=['zojax'],
      install_requires = ['setuptools',
                          'zope.component',
                          'zope.interface',
                          'zope.security',
                          'zope.schema',
                          'zope.i18n',
                          'zope.proxy',
                          'zope.size',
                          'zope.location',
                          'zope.publisher',
                          'zope.traversing',
                          'zope.lifecycleevent',
                          'zope.app.publication',
                          'zope.pagetemplate',
                          'zope.app.pagetemplate',
                          'zope.app.container',

                          'z3c.form',
                          'z3c.traverser',
                          'z3c.breadcrumb',

                          'zojax.layout',
                          'zojax.layoutform',
                          'zojax.controlpanel',
                          'zojax.content.type',
                          'zojax.content.model',
                          ],
      extras_require = dict(test=['zope.app.testing',
                                  'zope.app.zcmlfiles',
                                  'zope.app.rotterdam',
                                  'zope.securitypolicy',
                                  'zope.testing',
                                  'zope.testbrowser',
                                  'zojax.autoinclude',
                                  'zojax.content.browser',
                                  ]),
      include_package_data = True,
      zip_safe = False
      )
