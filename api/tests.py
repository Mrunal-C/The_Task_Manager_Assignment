""" from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task

class TaskAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

    def test_create_task(self):
        response = self.client.post('/api/tasks/', {
            'title': 'Test Task',
            'description': 'Test Description',
            'status': 'Todo',
            'priority': 'High',
            'due_date': '2024-07-31'
        },format='json')
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Test Task')
"""   

from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Task

class TaskAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)  

    def test_create_task(self):
        url = '/api/tasks/'
        data = {
            "title": "New Task",
            "description": "Task description",
            "status": "Todo",
            "priority": "High",
            "due_date": "2024-07-31",
            "user": self.user.id  
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])

        # Additional checks to verify data creation
        task_id = response.data['id']
        created_task = Task.objects.get(id=task_id)
        print(f'Task Created: {created_task.title}, Status: {created_task.status}, Assigned to: {created_task.user.username}')

        # Assertions to confirm the task was created as expected
        self.assertEqual(created_task.title, data['title'])
        self.assertEqual(created_task.status, data['status'])
        self.assertEqual(created_task.user, self.user)
