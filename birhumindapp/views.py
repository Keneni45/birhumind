from rest_framework import viewsets, generics
from .models import  NewsArticle, News, OurService, UserProfile, OurSuccess, Tutorial, Consultancy, AccessToFinance
from .serializers import NewsArticleSerializer, NewsSerializer, OurServiceSerializer, UserRegistrationSerializer, OurSuccessSerializer, TutorialSerializer, ConsultancySerializer, AccessToFinanceSerializer

class AccessToFinanceViewset(viewsets.ModelViewSet):
    queryset=AccessToFinance.objects.all()
    serializer_class=AccessToFinanceSerializer
class ConsultancyViewset(viewsets.ModelViewSet):
    queryset=Consultancy.objects.all()
    serializer_class=ConsultancySerializer
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer  # Use the correct attribute

    def perform_create(self, serializer):
        serializer.save()
class NewsArticleViewSet(viewsets.ModelViewSet):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerializer
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
