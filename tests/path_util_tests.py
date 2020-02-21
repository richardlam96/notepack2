import os
import unittest
from pathlib import Path
from notepack import config
from notepack.utility import path as path_util


class PathUtilTests(unittest.TestCase):

    def setUp(self):
        self.root_dir = path_util.get_root_path()
        self.test_dirname = 'testdir'
        self.test_filename = 'description.md'

    def test_create_dir_in_path(self):
        new_dir = path_util.create_dir_in_path(self.root_dir, 
                                               self.test_dirname)
        expected_dir = self.root_dir.joinpath(self.test_dirname)
        self.assertEqual(new_dir, expected_dir)

    def test_create_file_in_path(self):
        new_file = path_util.copy_file_to_path(self.root_dir, 
                                               self.test_filename)
        expected_filepath = self.root_dir.joinpath(self.test_filename)
        self.assertEqual(new_file, expected_filepath)

    def tearDown(self):
        self.root_dir.joinpath(self.test_dirname).rmdir()
        self.root_dir.joinpath(self.test_filename).unlink()


