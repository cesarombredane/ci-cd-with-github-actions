import unittest
from src.app import app

bad_response_200 = 'response should be 200'

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_read_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200, bad_response_200)

    def test_add_item(self):
        response = self.app.post('/add', data=dict(item='test'), follow_redirects=True)
        self.assertEqual(response.status_code, 200, bad_response_200)
        if response.text.find('test') == -1: self.fail('item not returned')

    def test_delete_item(self):
        response = self.app.get('/delete/0', follow_redirects=True)
        self.assertEqual(response.status_code, 200, bad_response_200)
        
    def test_update_item(self):
        response = self.app.post('/add', data=dict(item='test'), follow_redirects=True)
        self.assertEqual(response.status_code, 200, bad_response_200)
        response = self.app.post('/update/0', data=dict(new_item='test2'), follow_redirects=True)
        self.assertEqual(response.status_code, 200, bad_response_200)
        if response.text.find('test2') == -1: self.fail('updated item not returned')

if __name__ == '__main__':
    unittest.main()