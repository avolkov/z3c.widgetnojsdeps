##############################################################################
#
# Copyright (c) 2006 Zope Foundation and Contributors.
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
"""Optional Dropdown Widget Tests."""

from pprint import pprint
from zope.app.testing import placelesssetup
from z3c.widgetnojsdeps.optdropdown.test_optdropdown import TestFieldIntegration
import doctest
import unittest2 as unittest

def run_unittests():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFieldIntegration)
    unittest.TextTestRunner(verbosity=2).run(suite)
def test_suite():
    run_unittests()
    return doctest.DocFileSuite(
        'README.txt',
        setUp=placelesssetup.setUp, tearDown=placelesssetup.tearDown,
        globs={'pprint': pprint},
        optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS)
