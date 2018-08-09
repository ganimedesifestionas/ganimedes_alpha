# config.py
class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments

class SandBoxConfig(Config):
    """
    Development configurations
    """
    DEBUG = True
    TESTING = True
    SQLALCHEMY_ECHO = True
    globalDebugLevel = 1
    globalDebugLevelStartFinish = 1
    globalDebugLevelSection = 1
    globalDebugLevelError = 1
    globalDebugLevelMessage = 1
    globalDebugLevelInputParam = 1
    globalDebugLevelValue = 1
    globalDebugLevelResults = 1
    globalDebugLevelHttp = 1

class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEBUG = True
    TESTING = True
    SQLALCHEMY_ECHO = True
    globalDebugLevel = 1
    globalDebugLevelStartFinish = 1
    globalDebugLevelSection = 1
    globalDebugLevelError = 1
    globalDebugLevelMessage = 1
    globalDebugLevelInputParam = 1
    globalDebugLevelValue = 1
    globalDebugLevelResults = 1
    globalDebugLevelHttp = 1

class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_ECHO = False
    globalDebugLevel = 0
    globalDebugLevelStartFinish = 0
    globalDebugLevelSection = 0
    globalDebugLevelError = 0
    globalDebugLevelMessage = 0
    globalDebugLevelInputParam = 0
    globalDebugLevelValue = 0
    globalDebugLevelResults = 0
    globalDebugLevelHttp = 0

class TestingConfig(Config):
    """
    Testing configurations
    """
    DEBUG = False
    TESTING = True
    SQLALCHEMY_ECHO = False
    globalDebugLevel = 0
    globalDebugLevelStartFinish = 0
    globalDebugLevelSection = 0
    globalDebugLevelError = 0
    globalDebugLevelMessage = 0
    globalDebugLevelInputParam = 0
    globalDebugLevelValue = 0
    globalDebugLevelResults = 0
    globalDebugLevelHttp = 0

app_config = {
    'sandbox' : SandBoxConfig,
    'development' : DevelopmentConfig,
    'production' : ProductionConfig
}

