from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from .models import Snippet
from django.contrib.auth.models import User
from rest_framework import status

class NewsTest(APITestCase):

   def setUp(self):
       pass

   def test_post_snippet(self):
       data = {"code":"ff"}
       response = self.client.post('http://localhost:8000/snippetzz/', data)
       self.assertEqual(response.status_code, status.HTTP_201_CREATED)

   def test_get_snippets(self):
       response = self.client.get('http://localhost:8000/snippetzz/')
       self.assertEqual(response.status_code, status.HTTP_200_OK)

   def test_get_a_snippet(self):
       data = {"code":"ff"}
       self.client.post('http://localhost:8000/snippetzz/', data)
       response = self.client.get('http://localhost:8000/snippetzz/1/')
       self.assertEqual(response.status_code, status.HTTP_200_OK)

   def test_no_snippet(self):
       response = self.client.get('http://localhost:8000/snippetzz/1/')
       self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

   def test_add_user(self):
       data = {"username":"joel"}
       response = self.client.post('http://localhost:8000/users/', data)
       self.assertEqual(response.status_code, status.HTTP_201_CREATED) 

   def test_get_users(self):
       data = {"username":"joel"}
       self.client.post('http://localhost:8000/users/', data)
       response = self.client.get('http://localhost:8000/users/', data)
       self.assertEqual(response.status_code, status.HTTP_200_OK) 

   def test_get_a_user(self):
       data = {"username":"joel"}
       self.client.post('http://localhost:8000/users/', data)
       response = self.client.get('http://localhost:8000/users/2/', data)
       self.assertEqual(response.status_code, status.HTTP_200_OK) 

   def test_no_user(self):
       data = {"username":"joel"}
       self.client.post('http://localhost:8000/users/', data)
       response = self.client.get('http://localhost:8000/users/24/', data)
       self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND) 