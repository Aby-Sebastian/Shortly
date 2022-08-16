from django.test import TestCase
from anonymous_data.models import AnonymousUsersLink
import uuid
from django.utils import timezone

# Create your tests here.


class AnonymousModelTest(TestCase):
	def setUp(self):
		self.ad=AnonymousUsersLink.objects.create(url='https://docs.djangoproject.com/en/4.0/ref/contrib/auth/#module-django.contrib.auth.backends',short_url=str(uuid.uuid4())[:5],expiration_date=timezone.now() + timezone.timedelta(minutes=5))

	def test_links(self):
		obj = AnonymousUsersLink.objects.get(url='https://docs.djangoproject.com/en/4.0/ref/contrib/auth/#module-django.contrib.auth.backends')
		self.assertEqual(obj,self.ad)

	def test_links(self):
		obj = AnonymousUsersLink.objects.get(url='https://docs.djangoproject.com/en/4.0/ref/contrib/auth/#module-django.contrib.auth.backends')
		self.assertTrue(obj.set_expiration_date(),self.ad.expiration_date)