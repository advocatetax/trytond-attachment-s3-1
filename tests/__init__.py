# -*- coding: utf-8 -*-
"""
    __init__

    Test Suite for the attachment S3 module

"""
import unittest

import trytond.tests.test_tryton

from .test_view_and_depends import TestViewDependsCase


def suite():
    test_suite = trytond.tests.test_tryton.suite()
    test_suite.addTests(
        unittest.TestLoader().loadTestsFromTestCase(TestViewDependsCase)
    )
    return test_suite
