from statistics import mode
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Gallery(models.Model):
	image = models.ImageField(upload_to='gallery/%Y/%m/%d/')
	alt = models.CharField(max_length=50)
	user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
	
	class Meta:
		ordering=["-id"]

	def __str__(self):
		return self.alt
		
