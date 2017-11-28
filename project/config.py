
class BaseConfig:
    """Base configuration"""
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY = 'my_precious'
    BCRYPT_LOG_ROUNDS = 13
    TOKEN_EXPIRATION_DAYS = 30
    TOKEN_EXPIRATION_SECONDS = 0
    REGISTER_DEACTIVATED = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://'
