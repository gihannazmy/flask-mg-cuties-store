# db configration
class Config:

    pass



class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///devdatabase.db"


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///proddatabase.db"


configuration_options = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}
