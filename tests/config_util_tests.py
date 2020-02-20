import unittest
from notepack import config
from notepack.utility import config as config_util


class ConfigUtilTests(unittest.TestCase):

    def test_get_entities(self):
        self.assertEqual(config_util.get_entities(), config.ENTITIES.keys())

    def test_get_directories_for_notepack(self):
        for entity in config.ENTITIES: self.assertEqual(config_util.get_directory_names(entity),
                             config.ENTITIES[entity]['directories'])

    def test_get_directories_for_notepack(self):
        for entity in config.ENTITIES:
            self.assertEqual(config_util.get_file_names(entity),
                             config.ENTITIES[entity]['files'])


