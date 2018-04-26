#!/usr/bin/python
import yaml


with open("config.dev.yml", 'r') as stream:
    try:
        vars = yaml.load(stream)

        for k, v in vars.items():
            print('export {}={}'.format(k, v))
    except yaml.YAMLError as exc:
        print(exc)
