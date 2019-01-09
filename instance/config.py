import os

class config(object):
    DEBUG: False
    CSRF_ENABLED: True

class developmentConfig(config):
    DEBUG: True

class stagingConfig(config):
    DEBUG: True

class testingConfig(config):
    TESTING: True
    DEBUG: True

class productionConfig(config):
    DEBUG: False
    TESTING: False

app_config = {
    'development': developmentConfig,
    'testing': testingConfig,
    'staging': stagingConfig,
    'production': productionConfig,
}