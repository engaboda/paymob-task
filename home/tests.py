from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core import mail
# Create your tests here.
User = get_user_model()

class UserTestCase(TestCase):
    """ 
        test registering new user.
        test system user can login in.
    """
    def test_create_user_through_api(self):
        url = '/api/users/'
        data = {
            'email': 'test@yahoo.com',
            'password': 'password',
            'username': 'test'
        }
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(data.get('email'), resp.data.get('email'))
        self.assertEqual(data.get('username'), resp.data.get('username'))

    def test_user_can_get_token_or_user_can_login(self):
        user = User.objects.create_user(username='aboda', password='123456789*/')
        url = '/api/users/'
        self.client.force_login(user)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'refresh')
        self.assertContains(resp, 'token')

    def test_user_get_email(self):
        url = '/api/users/'
        data = {
            'email': 'test@yahoo.com',
            'password': 'password',
            'username': 'test'
        }
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(len(mail.outbox), 1)