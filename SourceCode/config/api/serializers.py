from rest_framework import serializers
from api.models import *
from django.db.models import Q


class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = ('telephoneNumber',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('url', 'email', 'first_name', 'last_name', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.telephoneNumber = profile_data.get('telephoneNumber', profile.telephoneNumber)
        profile.save()

        return instance


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('article_id', 'title', 'content', 'content_short', 'source_uri', 'image_uri', 'display_time', 'importance', 'created_date', 'updated_date', 'is_delete')
        read_only_fields = ['article_id']

    def create(self, validated_data):

        article = Article(**validated_data)
        article.save()

        return article

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content_short = validated_data.get('content_short', instance.content_short)
        instance.content = validated_data.get('content', instance.content)
        instance.source_uri = validated_data.get('source_uri', instance.source_uri)
        instance.image_uri = validated_data.get('image_uri', instance.image_uri)
        instance.display_time = validated_data.get('display_time', instance.display_time)
        instance.importance = validated_data.get('importance', instance.importance)
        instance.is_delete = validated_data.get('is_delete', instance.is_delete)
        instance.save()

        return instance


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ('status_id', 'name', 'is_active', 'is_delete')
        read_only_fields = ['status_id']

    def create(self, validated_data):

        status = Status(**validated_data)
        status.save()

        return status

    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_delete = validated_data.get('is_delete', instance.is_delete)
        instance.save()

        return instance


class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = ('region_id', 'name', 'is_active', 'is_delete')
        read_only_fields = ['region_id']

    def create(self, validated_data):

        region = Region(**validated_data)
        region.save()

        return region

    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_delete = validated_data.get('is_delete', instance.is_delete)
        instance.save()

        return instance


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ('game_id', 'name', 'uri_name', 'description', 'icon_uri', 'is_active', 'is_delete')
        read_only_fields = ['game_id']

    def create(self, validated_data):

        game = Game(**validated_data)
        game.save()

        return game

    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.uri_name = validated_data.get('uri_name', instance.uri_name)
        instance.description = validated_data.get('description', instance.description)
        instance.icon_uri = validated_data.get('icon_uri', instance.icon_uri)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_delete = validated_data.get('is_delete', instance.is_delete)
        instance.save()

        return instance


class LeagueSerializer(serializers.ModelSerializer):

    class Meta:
        model = League
        fields = ('league_id', 'name', 'uri_name', 'description', 'price_pool', 'starting_date', 'banner_in_list_uri', 'banner_in_detail_uri', 'league_status', 'league_game', 'is_active', 'is_delete')
        read_only_fields = ['league_id']

    def create(self, validated_data):

        league = League(**validated_data)
        league.save()

        return league

    def update(self, instance, validated_data):

        instance.name = validated_data.get('name', instance.name)
        instance.uri_name = validated_data.get('uri_name', instance.uri_name)
        instance.description = validated_data.get('description', instance.description)
        instance.price_pool = validated_data.get('price_pool', instance.price_pool)
        instance.starting_date = validated_data.get('starting_date', instance.starting_date)
        instance.banner_in_list_uri = validated_data.get('banner_in_list_uri', instance.banner_in_list_uri)
        instance.banner_in_detail_uri = validated_data.get('banner_in_detail_uri', instance.banner_in_detail_uri)
        instance.league_status = validated_data.get('league_status', instance.league_status)
        instance.league_game = validated_data.get('league_game', instance.league_game)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_delete = validated_data.get('is_delete', instance.is_delete)
        instance.save()

        return instance


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = ('team_id', 'name', 'short_name', 'uri_name', 'description', 'world_rank', 'region_rank', 'total_earnings',
                 'win_rate', 'starting_date', 'banner_in_list_uri', 'banner_in_detail_uri', 'team_region', 'is_active', 'is_delete')
        read_only_fields = ['team_id']

    def create(self, validated_data):
        
        try:
            world_rank_val = int(validated_data.pop('world_rank'))
        except ValueError:
            world_rank_val = None
        
        try:
            region_rank_val = int(validated_data.pop('region_rank'))
        except ValueError:
            region_rank_val = None

        try:
            existed = Team.objects.get(Q(world_rank=world_rank_val))
        except Team.DoesNotExist:
            existed = None

        if existed is None:
            team = Team(**validated_data)
            team.world_rank = world_rank_val
            team.region_rank = region_rank_val
            team.save()
        else:
            team = Team()

        return team

    def update(self, instance, validated_data):
        
        try:
            world_rank_val = int(validated_data.pop('world_rank'))
        except ValueError:
            world_rank_val = None
        
        try:
            region_rank_val = int(validated_data.pop('region_rank'))
        except ValueError:
            region_rank_val = None

        try:
            existed = Team.objects.get(Q(world_rank=world_rank_val) | Q(region_rank=region_rank_val))
        except Team.DoesNotExist:
            existed = None

        if existed is None:
            instance.name = validated_data.get('name', instance.name)
            instance.short_name = validated_data.get('short_name', instance.short_name)
            instance.uri_name = validated_data.get('uri_name', instance.uri_name)
            instance.description = validated_data.get('description', instance.description)
            instance.world_rank = world_rank_val
            instance.region_rank = region_rank_val
            instance.total_earnings = validated_data.get('total_earnings', instance.total_earnings)
            instance.win_rate = validated_data.get('win_rate', instance.win_rate)
            instance.starting_date = validated_data.get('starting_date', instance.starting_date)
            instance.banner_in_list_uri = validated_data.get('banner_in_list_uri', instance.banner_in_list_uri)
            instance.banner_in_detail_uri = validated_data.get('banner_in_detail_uri', instance.banner_in_detail_uri)
            instance.team_region = validated_data.get('team_region', instance.team_region)
            instance.is_active = validated_data.get('is_active', instance.is_active)
            instance.is_delete = validated_data.get('is_delete', instance.is_delete)
            instance.save()

        return instance


class MatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Match
        fields = ('match_id', 'uri_name', 'starting_date', 'team_left', 'team_right', 'is_active', 'is_delete', 'match_status', 'match_league')
        read_only_fields = ['match_id']

    def create(self, validated_data):
        
        match = Match(**validated_data)
        match.save()

        return match

    def update(self, instance, validated_data):

        instance.uri_name = validated_data.get('uri_name', instance.uri_name)
        instance.starting_date = validated_data.get('starting_date', instance.starting_date)
        instance.team_left = validated_data.get('team_left', instance.team_left)
        instance.team_right = validated_data.get('team_right', instance.team_right)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_delete = validated_data.get('is_delete', instance.is_delete)
        instance.match_status = validated_data.get('match_status', instance.match_status)
        instance.match_league = validated_data.get('match_league', instance.match_league)
        instance.save()

        return instance