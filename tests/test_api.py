import os
import unittest
import tempfile

from webhook_publisher import api


class APITestCase(unittest.TestCase):
    def setUp(self):
        api.app.testing = True
        self.app = api.app.test_client()

    def test_api_loads(self):
        result = self.app.get('/version', follow_redirects=True)
        assert result.status_code == 200
        assert result.data == b'{\n  "message": "0.0.1"\n}\n'

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
