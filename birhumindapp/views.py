from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import News, OurService,  OurSuccess, Tutorial, Consultancy, AccessToFinance,  Tutorial_Instructor
from .serializers import  DocumentSubmissionSerializer, NewsSerializer, OurServiceSerializer,  OurSuccessSerializer, TutorialSerializer, ConsultancySerializer, AccessToFinanceSerializer, UserProfileSerializer, Tutorial_InstructorSerializer




class DocumentSubmissionView(APIView):
    def post(self, request, *args, **kwargs):
        # Deserialize the request data
        serializer = DocumentSubmissionSerializer(data=request.data)
        
        if serializer.is_valid():
            # Save the new document submission to the database
            submission = serializer.save()
            return Response({"message": "Form submitted successfully", "submission_id": submission.id}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Tutorial_InstructorViewset(viewsets.ModelViewSet):
    queryset=Tutorial_Instructor.objects.all()
    serializer_class=Tutorial_InstructorSerializer
class AccessToFinanceViewset(viewsets.ModelViewSet):
    queryset=AccessToFinance.objects.all()
    serializer_class=AccessToFinanceSerializer
class ConsultancyViewset(viewsets.ModelViewSet):
    queryset=Consultancy.objects.all()
    serializer_class=ConsultancySerializer

class RegisterUser(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TutorialViewSet(viewsets.ModelViewSet):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer
class OurSuccessViewSet(viewsets.ModelViewSet):
    queryset = OurSuccess.objects.all()
    serializer_class = OurSuccessSerializer
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class OurServiceViewSet(viewsets.ModelViewSet):
    queryset=OurService.objects.all()
    serializer_class=OurServiceSerializer

