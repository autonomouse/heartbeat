#!/usr/bin/env python3

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    base = os.path.abspath(os.path.dirname(__file__))
    DEVELOPMENT = True
    DEBUG = True
    CSRF_ENABLED = True
    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'a very secret string'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base, 'app.sqlite')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(base, 'db_repository')
    STATIC_DIR = './static'


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False


class TestingConfig(Config):
    DEVELOPMENT = False
    DEBUG = False


env_var = os.environ.get('FlaskConfigName')
config = {
    'Development': DevelopmentConfig,
    'Testing': TestingConfig,
    'Staging': StagingConfig,
    'Production': ProductionConfig,
    }.get(env_var, TestingConfig)
