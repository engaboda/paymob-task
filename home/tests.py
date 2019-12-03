from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core import mail
from .models import PostModel
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


class PostTestCases(TestCase):
    """
        test user can create post or view his or another user post
    """
    def setUp(self):
        self.user = User.objects.create_user(username='aboda', password='12456789/')

    def test_user_can_create_post(self):
        url = '/api/posts/'
        data = {
            'text': 'Welcome ya bro'
        }
        self.client.force_login(self.user)
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(data.get('text'), resp.data.get('text'))
    
    def test_user_can_list_all_posts(self):
        url = '/api/posts/'
        PostModel.objects.create(user=self.user)
        PostModel.objects.create(user=self.user)
        PostModel.objects.create(user=self.user)
        PostModel.objects.create(user=self.user)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data), 4)
