from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    telephoneNumber = models.CharField(max_length=20, blank=True)

class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    content = models.CharField(max_length=4000)
    content_short = models.CharField(max_length=2000)
    source_uri = models.URLField(blank=True)
    image_uri = models.URLField(blank=True)
    display_time = models.DateTimeField()
    importance = models.SmallIntegerField()
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)