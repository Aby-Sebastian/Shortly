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
		
	def get_size(self):
		val = self.image.size
		for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
			if val < 1024.0:
				return "%3.1f %s" % (val, x)
			val /= 1024.0

		return val
	
	def save(self, *args, **kwargs):
		
		super(Gallery, self).save(*args, **kwargs)