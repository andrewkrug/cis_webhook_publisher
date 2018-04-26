# CIS Webhook Publisher

## Setting up a local environment with serverlesss

1. `npm install -g serverless`
2. `cd webhook_publisher/`
3. `sls plugin install -n serverless-wsgi`
4. `sls plugin install -n serverless-python-requirements`
5. `sls plugin install -n serverless-domain-manager`
6. `setup a virtualenv`
7. `pip3 install -r requirements.txt`

## Deploying

`sls deploy --stage prod --region us-west-2`
`sls deploy --stage dev --region us-west-2`

## First time in a new AWS Account Only

1. Create an ACM Certificate for the domain.
2. `serverless --stage dev create_domain` | `serverless --stage prod create_domain`

## Running flask locally using serverless wsgi

`sls wsgi serve`

## Running the tests

`pip3 install nose nose-watch`
`python3 -m unittest discover tests` or `nosetests --with-watch tests/`
