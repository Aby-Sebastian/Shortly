from django.test import TestCase

# Create your tests here.
class FilesUrlTest(TestCase):
    def test_files(self):
        response = self.client.get('/files/')
        self.assertEqual(response.status_code, 200)
    
class DashboardUrlTest(TestCase):
    def test_analytics(self):
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)

class IndexUrlTest(TestCase):
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class GalleryUrlTest(TestCase):
    def test_index(self):
        response = self.client.get('/gallery/')
        self.assertEqual(response.status_code, 200)
