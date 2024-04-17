from flask_testing import TestCase
from project import db, create_app


class BaseTestCase(TestCase):
    def create_app(self):
        return create_app()

    def setUp(self):
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
