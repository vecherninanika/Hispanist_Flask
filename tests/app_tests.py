import os
import unittest
import tempfile
import sys

from flask import app
sys.path.append('./')
import manage

# def init_db():
#     with app.app_context():
#         db = get_db()
#         with app.open_resource('schema.sql', mode='r') as f:
#             db.cursor().executescript(f.read())
#         db.commit()


class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, manage.app.config['DATABASE'] = tempfile.mkstemp()
        manage.app.config['TESTING'] = True
        self.app = manage.app.test_client()
        # manage.app.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(manage.app.config['DATABASE'])

    def test_empty_db(self):
        rv = self.app.get('/')
        print(rv.data)
        assert '<title>Hispanist</title>' in rv.data

if __name__ == '__main__':
    unittest.main()
