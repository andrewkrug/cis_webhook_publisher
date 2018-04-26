import unittest

from webhook_publisher import idp_users


class AuthZeroTestCase(unittest.TestCase):
    def test_query_all_users(self):
        a = idp_users.People()
        print(a.all)

        assert 0
