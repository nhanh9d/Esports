from rest_framework import serializers
from api.models import User, UserProfile, Article


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
        fields = ('article_id', 'title', 'content', 'content_short', 'source_uri', 'image_uri', 'display_time', 'importance', 'created_date', 'updated_date')
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
        instance.save()

        return instance