import unittest
from .config_util_tests import ConfigUtilTests


def suite():
    """Run all desired tests."""
    main_suite = unittest.TestSuite()
    main_suite.addTest(unittest.makeSuite(ConfigUtilTests))
    main_suite.debug()

suite()
