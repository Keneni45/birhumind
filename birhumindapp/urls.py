from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsArticleViewSet, NewsViewSet, OurServiceViewSet, UserRegistrationView, OurSuccessViewSet, TutorialViewSet, ConsultancyViewset, AccessToFinanceViewset

router = DefaultRouter()
router.register('news', NewsArticleViewSet)
router.register('oduu', NewsViewSet)
router.register('service', OurServiceViewSet)
router.register('success', OurSuccessViewSet)
router.register('tutorials', TutorialViewSet)
router.register('consultancy', ConsultancyViewset)
router.register('finance', AccessToFinanceViewset)





urlpatterns = [
    path('', include(router.urls)),
    path('registration/', UserRegistrationView.as_view(), name='registration')
]