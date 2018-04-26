
import boto3

from authzero import AuthZero
from webhook_publisher import config

class People(object):
    def __init__(self):
        self.config = config.get_config()
        self.client_id = self.config('client_id')
        self.client_secret = config.get_encrypted_parameter(
            '/iam/cis/webhook_publisher_client_secret'
        )

    @property
    def all(self):
        config = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'uri': self.config('auth0_url')
        }

        authzero_client = AuthZero(config)
        authzero_client.get_access_token()
        users = authzero_client.get_users(query_filter='*')
        return users
