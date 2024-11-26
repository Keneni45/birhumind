from rest_framework import serializers
from .models import DocumentSubmission, Subscription, News, DocumentSubmission, OurService, UserProfile, OurSuccess, Tutorial, Consultancy, AccessToFinance, Tutorial_Instructor
from django.contrib.auth.models import User

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['email']

class DocumentSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentSubmission
        fields = ['name', 'institution', 'education_level', 'document_type', 'selected_documents', 'selected_templates']

    def validate(self, data):
        if not data.get('selected_documents'):
            raise serializers.ValidationError("At least one document type must be selected.")
        return data

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
class Tutorial_InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tutorial_Instructor
        fields= '__all__'
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'age', 'gender', 'education_level']