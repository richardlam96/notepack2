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

    def test_create_dir_in_path(self):
        new_dir = path_util.create_dir_in_path(self.root_dir, 
                                               self.test_dirname)
        self.assertEqual(new_dir, self.test_dir_path)

    def test_create_file_in_path(self):
        new_file = Path(path_util.create_template_copy(self.root_dir, 
                                                  self.test_filename))
        self.assertEqual(new_file, self.test_file_path)

    def tearDown(self):
        self.cleanUpTestResults()

    def cleanUpTestResults(self):
        if self.test_dir_path.exists(): self.test_dir_path.rmdir()
        if self.test_file_path.exists(): self.test_file_path.unlink()


