from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import News, OurService,  OurSuccess, Tutorial, Consultancy, AccessToFinance, UserProfile
from .serializers import NewsSerializer, OurServiceSerializer,  OurSuccessSerializer, TutorialSerializer, ConsultancySerializer, AccessToFinanceSerializer, UserProfileSerializer

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
# Create your views here.
