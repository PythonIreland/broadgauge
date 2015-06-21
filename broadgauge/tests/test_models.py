import unittest
import web
from broadgauge.models import User, get_db
import os

class DBTestCase(unittest.TestCase):
    def setUp(self):
        # clear the memoize cache
        get_db.cache.clear()
        web.config.db_parameters = dict(dbn='sqlite', db=":memory:")        
        self.load_schema()
    
    def tearDown(self):
        get_db.cache.clear()

    def load_schema(self):
        db = get_db()
        sql = self.read_schema()
        # what is called seial in postgres is called integer in sqlite
        sql = sql.replace("serial", "integer")

        # sqlite can execute only one statement in a query
        for part in sql.split(";"):
            db.query(part)

    def read_schema(self):
        dirname = os.path.dirname
        root = dirname(dirname(__file__))
        return open(os.path.join(root, "schema.sql")).read()

class UserTest(DBTestCase):
    def setUp(self):
        get_db.cache.clear()
        self.name = 'User 1'
        self.email = 'user1@example.com'
        self.phone = '1234567890'

        #Create user default
        self.user = User.new(name=self.name, email=self.email, phone=self.phone)

    def tearDown(self):
        #Remove the user default
        get_db().delete("users", where="id =" + str(self.user.id))

    def test_success(self):
        self.assertTrue(True)

    def test_new_saves_user(self):
        self.assertEquals(self.user.name, self.name)
        self.assertEquals(self.user.email, self.email)
        self.assertEquals(self.user.phone, self.phone)
        self.assertNotEquals(self.user.id, None)

    def test_find_returns_user(self):
        self.assertEquals(User.find(id=self.user.id), self.user)

    def test_update_changes_user_and_update_on_database(self):
        self.user.update(name='User 2')
        self.assertEquals(self.user.name, 'User 2')
        self.assertEquals(User.find(id=self.user.id).name, 'User 2')

if __name__ == '__main__':
    unittest.main()
