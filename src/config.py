# -*- coding: utf-8 -*-
import os



DATABASE_NAME = './db.sqlite3'  # Файл с базой данных
SHELVE_NAME = 'shelve.db'  #
SHELVE_LEVEL = 'shelve_level.db'  #

import os
from dataclasses import dataclass

import yaml
from marshmallow_dataclass import class_schema


@dataclass
class Config:
    ALLOWED_HOSTS: list
    SECRET_KEY: str
    DEBUG: bool
    SWAGGER_TITLE: str
    SWAGGER_DESCRIPTION: str
    DATABASE_NAME: str
    SHELVE_NAME: str
    SHELVE_LEVEL: str


config_path = "/../config.yaml"
if os.getenv("IS_TEST", False):
    config_path = "/../config.example.yaml"

with open(os.path.dirname(__file__) + config_path) as f:
    config_data = yaml.safe_load(f)

config: Config = class_schema(Config)().load(config_data)
