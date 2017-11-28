import unittest
import os
from flask import current_app
from flask_testing import TestCase

from project import create_app

app = create_app()


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.config.BaseConfig')
        app.config.from_envvar('APP_DEVELOPMENT_CONFIG')
        return app

    def test_app_is_development(self):
        self.assertTrue(
            app.config['SECRET_KEY'] ==
            'my_precious'
        )

        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] ==
            'mysql+pymysql://' + os.environ.get('DB_LOGIN') + '@localhost/user_service'
        )
        self.assertTrue(app.config['BCRYPT_LOG_ROUNDS'] == 4)
        self.assertTrue(app.config['TOKEN_EXPIRATION_DAYS'] == 30)
        self.assertTrue(app.config['TOKEN_EXPIRATION_SECONDS'] == 0)
        self.assertTrue(app.config['REGISTER_DEACTIVATED'] is False)


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.config.BaseConfig')
        app.config.from_envvar('APP_TEST_CONFIG')
        return app

    def test_app_is_testing(self):
        self.assertTrue(
            app.config['SECRET_KEY'] ==
            'my_precious'
        )

        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(app.config['TESTING'])
        self.assertFalse(app.config['PRESERVE_CONTEXT_ON_EXCEPTION'])
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] ==
            'mysql+pymysql://' + os.environ.get('DB_LOGIN') + '@localhost/user_service_test'
        )
        self.assertTrue(app.config['BCRYPT_LOG_ROUNDS'] == 4)
        self.assertTrue(app.config['TOKEN_EXPIRATION_DAYS'] == 0)
        self.assertTrue(app.config['TOKEN_EXPIRATION_SECONDS'] == 3)
        self.assertTrue(app.config['REGISTER_DEACTIVATED'] is False)


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.config.BaseConfig')
        app.config.from_envvar('APP_PRODUCTION_CONFIG')
        return app

    def test_app_is_production(self):
        self.assertTrue(
            app.config['SECRET_KEY'] ==
            'my_precious'
        )

        self.assertFalse(app.config['DEBUG'])
        self.assertFalse(app.config['TESTING'])
        self.assertTrue(app.config['BCRYPT_LOG_ROUNDS'] == 13)
        self.assertTrue(app.config['TOKEN_EXPIRATION_DAYS'] == 30)
        self.assertTrue(app.config['TOKEN_EXPIRATION_SECONDS'] == 0)
        self.assertTrue(app.config['REGISTER_DEACTIVATED'])


if __name__ == '__main__':
    unittest.main()
