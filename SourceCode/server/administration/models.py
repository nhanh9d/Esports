from django.db import models

# Create your models here.
class AdminUser(models.Model):
    userId = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    fullname = models.CharField(max_length=255)
    createDate = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name