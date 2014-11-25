from app import app
import unittest

class FlaskTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue('Please login' in response.data)

    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post(
                '/login',
                data=dict(username='admin', password='admin'),
                follow_redirects=True
                )
        self.assertIn('You were just logged in!', response.data)

    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post(
                '/login',
                data=dict(username='wrong', password='admin'),
                follow_redirects=True
                )
        self.assertIn('Invalid credentials. Please try again.', response.data)

    def test_logout(self):
        tester = app.test_client(self)
        tester.post(
                '/login',
                data=dict(username='admin', password='admin'),
                follow_redirects=True
                )
        response = tester.get('/logout', follow_redirects=True)
        self.assertIn('You were just logged out!', response.data)

    def test_main_page_requires_login(self):
        tester = app.test_client(self)
        response = tester.get('/', follow_redirects=True)
        self.assertTrue('You need to login first.' in response.data)

    def test_posts_in_main_page(self):
        tester = app.test_client(self)
        response = tester.post(
                '/login',
                data=dict(username='admin', password='admin'),
                follow_redirects=True
                )
        self.assertIn('Hello from the shell', response.data)

if __name__ == '__main__':
    unittest.main()
