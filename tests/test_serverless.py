import logging
import unittest
import yaml


logger = logging.getLogger(__name__)
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

class SLSYAMLTest(unittest.TestCase):
    def get_yaml_file(self):
        apps_yml = open('webhook_publisher/serverless.yml')
        contents = apps_yml.read()
        apps_yml.close()
        return contents

    def test_output_exists(self):
        assert self.get_yaml_file() is not None

    def test_yaml_loads(self):
        yaml_content = yaml.load(self.get_yaml_file())
        assert yaml_content is not None

class ProdConfigYAMLTest(unittest.TestCase):
    def get_yaml_file(self):
        apps_yml = open('webhook_publisher/config.prod.yml')
        contents = apps_yml.read()
        apps_yml.close()
        return contents

    def test_output_exists(self):
        assert self.get_yaml_file() is not None

    def test_yaml_loads(self):
        yaml_content = yaml.load(self.get_yaml_file())
        assert yaml_content is not None

class DevConfigYAMLTest(unittest.TestCase):
    def get_yaml_file(self):
        apps_yml = open('webhook_publisher/config.dev.yml')
        contents = apps_yml.read()
        apps_yml.close()
        return contents

    def test_output_exists(self):
        assert self.get_yaml_file() is not None

    def test_yaml_loads(self):
        yaml_content = yaml.load(self.get_yaml_file())
        assert yaml_content is not None
