from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

# Create your models here.

# Bảng người dùng
class User(AbstractUser):
    username = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)

# Thông tin thêm của bảng người dùng
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    telephoneNumber = models.CharField(max_length=20, blank=True)

# Bảng trạng thái
class Status(models.Model):
    status_id = models.AutoField(primary_key=True) #id
    name = models.CharField(max_length=256, blank=True,db_index=True) #tên

    is_active = models.BooleanField(default=True) #có dùng hay không
    is_delete = models.BooleanField(default=False) #đã xóa hay chưa
    
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True) #ngày tạo
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True) #ngày cập nhật

    def __str__(self):
        return self.name

class Region(models.Model):
    region_id = models.AutoField(primary_key=True) #id
    name = models.CharField(max_length=256, blank=True,db_index=True) #tên khu vực
    
    is_active = models.BooleanField(default=True) #có dùng hay không
    is_delete = models.BooleanField(default=False) #đã xóa hay chưa

    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True) #ngày tạo
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True) #ngày cập nhật

    def __str__(self):
        return self.name

# Bảng tin tức
class Article(models.Model):
    article_id = models.AutoField(primary_key=True) #id
    title = models.CharField(max_length=256,db_index=True) #tiêu đề
    content = models.CharField(max_length=4000) #nội dung
    content_short = models.CharField(max_length=2000) #tin vắn
    source_uri = models.URLField(blank=True) #tên trên thanh tiêu đề
    image_uri = models.URLField(blank=True) #đường dẫn ảnh
    display_time = models.DateTimeField() #thời gian hiển thị
    importance = models.SmallIntegerField() #mức độ quan trọng
    
    is_active = models.BooleanField(default=True) #có dùng hay không
    is_delete = models.BooleanField(default=False) #đã xóa hay chưa

    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True) #ngày tạo
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True) #ngày cập nhật

#Bảng game
class Game(models.Model):
    game_id = models.AutoField(primary_key=True) #id
    name = models.CharField(max_length=256,db_index=True) #tên trò chơi
    uri_name = models.CharField(max_length=256,db_index=True,blank=True) #tên trò chơi trên thanh url
    description = models.CharField(max_length=4000) #mô tả
    icon_uri = models.URLField(blank=True) #icon của game

    is_active = models.BooleanField(default=True) #có dùng hay không
    is_delete = models.BooleanField(default=False) #đã xóa hay chưa

    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True) #ngày tạo
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True) #ngày cập nhật

    def __str__(self):
        return self.name

#Bảng giải đấu
class League(models.Model):
    league_id = models.AutoField(primary_key=True) #id
    name = models.CharField(max_length=256,db_index=True) #tên giải đấu
    uri_name = models.CharField(max_length=256,db_index=True) #tên giải đấu trên thanh url
    description = models.CharField(max_length=4000) #mô tả
    price_pool = models.DecimalField(max_digits=19, decimal_places=10) #tổng giải thưởng
    starting_date = models.DateTimeField() #ngày bắt đầu giải
    banner_in_list_uri = models.URLField(blank=True) #ảnh banner hiển thị trong danh sách các giải đấu
    banner_in_detail_uri = models.URLField(blank=True) #ảnh banner hiển thị trong chi tiết của giải đấu

    #format = models.ForeignKey(Format, on_delete=models.CASCADE)
    #sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True) #có dùng hay không
    is_delete = models.BooleanField(default=False) #đã xóa hay chưa

    league_status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='league_status', blank=True, null=True) #trạng thái của giải đấu, khóa ngoại đến bảng trạng thái
    league_game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='league_game', blank=True, null=True) #trạng thái của giải đấu, khóa ngoại đến bảng trạng thái

    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True) #ngày tạo
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True) #ngày cập nhật

    def __str__(self):
        return self.name

#Bảng đội thi đấu
class Team(models.Model):
    team_id = models.AutoField(primary_key=True) #id
    name = models.CharField(max_length=256,db_index=True) #tên đội
    short_name = models.CharField(max_length=256, blank=True,db_index=True) #tên viết tắt đội
    uri_name = models.CharField(max_length=256) #tên trên thanh url
    description = models.CharField(max_length=4000) #mô tả
    world_rank = models.IntegerField(blank=True, null=True) #xếp hạng thế giới
    region_rank = models.IntegerField(blank=True, null=True) #xếp hạng khu vực
    total_earnings = models.DecimalField(max_digits=19, decimal_places=2) #tổng số tiền kiếm được
    win_rate = models.DecimalField(max_digits=19, decimal_places=6) #tỉ lệ thắng (%)
    starting_date = models.DateTimeField() #Ngày thành lập
    banner_in_list_uri = models.URLField(blank=True) #ảnh đội hiển thị trong list
    banner_in_detail_uri = models.URLField(blank=True) #ảnh đội hiển thị trong chi tiếtư

    is_active = models.BooleanField(default=True) #có dùng hay không
    is_delete = models.BooleanField(default=False) #đã xóa hay chưa

    team_region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True, related_name='team_region')

    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True) #ngày tạo
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True) #ngày cập nhật

    def __str__(self):
        return self.name

#Bảng trận đấu
class Match(models.Model):
    match_id = models.AutoField(primary_key=True) #id
    uri_name = models.CharField(max_length=256,db_index=True) #tên trên thanh url
    starting_date = models.DateTimeField() #thời gian bắt đầu thi đấu
    
    team_left = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='fk_match_team_left') #đội bên trái
    team_right = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='fk_match_team_right') #đội bên phải
    #best_of = models.ForeignKey(BestOf, on_delete=models.CASCADE)
    #match_type = models.ForeignKey(MatchType, on_delete=models.CASCADE)
    #status = models.ForeignKey(Status, on_delete=models.CASCADE) #trạng thái của trận đấu
    
    is_active = models.BooleanField(default=True) #có dùng hay không
    is_delete = models.BooleanField(default=False) #đã xóa hay chưa

    match_status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='match_status', blank=True, null=True) #trạng thái của trận đấu, khóa ngoại đến bảng trạng thái
    match_league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='match_league', blank=True, null=True) #giải đấu của trận đấu, khóa ngoại đến bảng trạng thái

    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True) #ngày tạo
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True) #ngày cập nhật