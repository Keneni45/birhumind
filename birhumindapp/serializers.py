from rest_framework import serializers
from .models import NewsArticle, News, OurService, UserProfile, OurSuccess, Tutorial, Consultancy
from django.contrib.auth.models import User

class ConsultancySerializer(serializers.ModelSerializer):
    class Meta:
        model=Consultancy
        fields='__all__'

class NewsArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArticle
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
class OurServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=OurService
        fields= '__all__'
class OurSuccessSerializer(serializers.ModelSerializer):
    class Meta:
        model=OurSuccess
        fields= '__all__'
class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tutorial
        fields= '__all__'
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('age', 'gender', 'education_level')

class UserRegistrationSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ('username', 'password', 'profile')

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')  # Extract profile data
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Hash the password
        user.save()  # Save the User instance

        # Create the UserProfile instance
        UserProfile.objects.create(user=user, **profile_data)
        return user