#!python
from setuptools import setup, find_packages
import os.path

def read(*path_elements):
    return "\n\n" + file(os.path.join(*path_elements)).read()

widget_path = 'widgetnojsdeps'
setup(name='z3c.widgetnojsdeps',
      version='0.3.1dev',
      author = "Zope Community",
      author_email = "avolkov@gmail.com",
      description = "Additional zope.formlib Widgets",
      license = "ZPL 2.1",
      keywords = "zope zope3 form formlib",
      url='https://github.com/avolkov/z3c.widgetnojsdeps',
      long_description=(
          '.. contents::\n\n' +
          read('CHANGES.txt') +
          read('src', 'z3c', widget_path, 'country', 'README.txt') +
          read('src', 'z3c', widget_path, 'dateselect', 'README.txt') +
          read('src', 'z3c', widget_path, 'dropdowndatewidget', 'README.txt') +
          read('src', 'z3c', widget_path, 'image', 'README.txt') +
          read('src', 'z3c', widget_path, 'namespace', 'README.txt') +
          read('src', 'z3c', widget_path, 'optdropdown', 'README.txt') +
          read('src', 'z3c', widget_path, 'sequence', 'README.txt') +
          read('src', 'z3c', widget_path, 'ssn', 'README.txt') +
          read('src', 'z3c', widget_path, 'usphone', 'README.txt')
          ),
      zip_safe=False,
      packages=find_packages('src'),
      include_package_data=True,
      package_dir = {'':'src'},
      namespace_packages=['z3c',],
      extras_require = dict(test=['zope.app.testing',
                                  'zope.testing',
                                  'zope.app.securitypolicy',
                                  'zope.app.zcmlfiles',
                                  'zope.testbrowser',
                                  ]),
      install_requires = ['setuptools',
                          'ZODB3',
                          'z3c.i18n',
                          'z3c.schema',
                          'z3c.form',
                          'zc.resourcelibrary',
                          'zope.app.cache',
                          'zope.app.container',
                          'zope.app.file',
                          'zope.app.i18n',
                          'zope.app.pagetemplate',
                          'zope.component',
                          'zope.event',
                          'zope.filerepresentation',
                          'zope.formlib >= 4.0',
                          'zope.i18n',
                          'zope.i18nmessageid',
                          'zope.interface',
                          'zope.lifecycleevent',
                          'zope.publisher',
                          'zope.schema',
                          'zope.security',
                          'zope.traversing',
                          ],
      classifiers = ['Development Status :: 4 - Beta',
                     'Environment :: Web Environment',
                     'Framework :: Zope3',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved :: Zope Public License',
                     'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
                     'Programming Language :: Python',
                     'Topic :: Software Development :: Libraries :: Python Modules',
                     ],
      )

