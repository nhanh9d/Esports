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

class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, blank=True,db_index=True)
    is_active = models.BooleanField(default=True)
    
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)

class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256,db_index=True)
    content = models.CharField(max_length=4000)
    content_short = models.CharField(max_length=2000)
    source_uri = models.URLField(blank=True)
    image_uri = models.URLField(blank=True)
    display_time = models.DateTimeField()
    importance = models.SmallIntegerField()
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)

class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256,db_index=True)
    uri_name = models.CharField(max_length=256,db_index=True)
    description = models.CharField(max_length=4000)
    icon_uri = models.URLField(blank=True)

    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)

class League(models.Model):
    league_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256,db_index=True)
    uri_name = models.CharField(max_length=256,db_index=True)
    description = models.CharField(max_length=4000)
    price_pool = models.DecimalField(max_digits=19, decimal_places=10)
    starting_date = models.DateTimeField()
    banner_in_list_uri = models.URLField(blank=True)
    banner_in_detail_uri = models.URLField(blank=True)

    #format = models.ForeignKey(Format, on_delete=models.CASCADE)
    #sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)

class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256,db_index=True)
    short_name = models.CharField(max_length=256, blank=True,db_index=True)
    uri_name = models.CharField(max_length=256)
    description = models.CharField(max_length=4000)
    world_rank = models.IntegerField()
    region_rank = models.IntegerField()
    total_earnings = models.DecimalField(max_digits=19, decimal_places=10)
    win_rate = models.DecimalField(max_digits=19, decimal_places=10)
    starting_date = models.DateTimeField()
    banner_in_list_uri = models.URLField(blank=True)
    banner_in_detail_uri = models.URLField(blank=True)

    #region = models.ForeignKey(Region, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)

class Match(models.Model):
    match_id = models.AutoField(primary_key=True)
    short_name = models.CharField(max_length=256, blank=True,db_index=True)
    uri_name = models.CharField(max_length=256)
    starting_date = models.DateTimeField()
    
    team_left = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='fk_match_team_left')
    team_right = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='fk_match_team_right')
    #best_of = models.ForeignKey(BestOf, on_delete=models.CASCADE)
    #match_type = models.ForeignKey(MatchType, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)

class Region(models.Model):
    region_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, blank=True,db_index=True)

    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)