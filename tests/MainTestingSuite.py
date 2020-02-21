import unittest
from .config_util_tests import ConfigUtilTests
from .path_util_tests import PathUtilTests


def suite():
    """Run all desired tests."""
    main_suite = unittest.TestSuite()
    main_suite.addTest(unittest.makeSuite(ConfigUtilTests))
    main_suite.addTest(unittest.makeSuite(PathUtilTests))
    main_suite.debug()

suite()
