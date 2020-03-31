import unittest
import FlaskProject


class TestBasic(unittest.TestCase):

    def setUp(self):
        FlaskProject.app.testing = True
        self.app = FlaskProject.app.test_client()

    def test_homepage(self):
        response = self.app.get('/', follow_redirects = True)
        self.assertEqual(response.status_code, 200)

    def test_rootpage(self):
        response = self.app.get('/home', follow_redirects = True)
        self.assertEqual(response.status_code, 200)

    def test_contactpage(self):
        response = self.app.get('/contact', follow_redirects = True)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
