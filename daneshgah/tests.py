import json

from django.test import TestCase
import rest_framework
from rest_framework.test import APIRequestFactory
# Create your tests here.

#basic test
# class MyTest(TestCase):
#     def setup(self):
#         print('testing')
#     def tearDown(self):
#         print('tearing down')
#     def testme(self):
#         print('hello')

factory = APIRequestFactory()
request = factory.post('/users/login', json.dump({'username': 'darya', 'password': '1234'}), content_type=
'application/json')
request1 = factory.post('/users/logout', content_type=
'application/json')
requestChangePassword = factory.post('/users/changePassword', json.dump({
    'username': 'darya',
    'password': '1234',
    'newPassword': '2468032'
}), content_type='application/json')