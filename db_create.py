#!/usr/bin/env python3

from migrate.versioning import api
from config import config
from app import db
import os.path
db.create_all()
if not os.path.exists(config.SQLALCHEMY_MIGRATE_REPO):
    api.create(config.SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(config.SQLALCHEMY_DATABASE_URI, config.SQLALCHEMY_MIGRATE_REPO, api.version(config.SQLALCHEMY_MIGRATE_REPO))
