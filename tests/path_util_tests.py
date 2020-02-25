import os
import unittest
from pathlib import Path
from notepack import config


class PathUtilTests(unittest.TestCase):

    def setUp(self):
        self.root_dir = path_util.get_root_path()
        self.test_dirname = 'testdir'
        self.test_filename = 'description.md'
        self.test_dir_path = self.root_dir.joinpath(self.test_dirname)
        self.test_file_path = self.root_dir.joinpath(self.test_filename)
        self.cleanUpTestResults()

    def tearDown(self):
        self.cleanUpTestResults()

    def cleanUpTestResults(self):
        if self.test_dir_path.exists(): self.test_dir_path.rmdir()
        if self.test_file_path.exists(): self.test_file_path.unlink()


