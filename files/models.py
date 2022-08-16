from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Files(models.Model):
    # description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='files/')
    share_url = models.CharField(max_length=50, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.document.name

    def get_size(self):
        val = self.document.size
        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if val < 1024.0:
                return "%3.1f %s" % (val, x)
            val /= 1024.0

        return val

    class Meta:
        verbose_name_plural = "Files"