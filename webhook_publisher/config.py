"""
:mod:`webhook_publisher.config` -- WebHook-Publisher configuration
* Environment variables used
 * API_AUDIENCE
 * AUTH0_URL
"""

import boto3
from everett.manager import ConfigManager
from everett.manager import ConfigOSEnv

def get_config():
    return ConfigManager([ConfigOSEnv()])

def connect_ssm():
    return boto3.client('ssm', region_name='us-west-2')

def get_encrypted_parameter(parameter_name):
    client = connect_ssm()

    result = client.get_parameter(
        Name=parameter_name,
        WithDecryption=True
    )

    parameter = result.get('Parameter')
    return parameter.get('Value')
