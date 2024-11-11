from rest_framework import serializers
from .models import News, OurService, UserProfile, OurSuccess, Tutorial, Consultancy, AccessToFinance
from django.contrib.auth.models import User


class AccessToFinanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=AccessToFinance
        fields='__all__'
class ConsultancySerializer(serializers.ModelSerializer):
    class Meta:
        model=Consultancy
        fields='__all__'
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
        fields = ['username', 'age', 'gender', 'education_level']