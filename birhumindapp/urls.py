from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet, OurServiceViewSet,  OurSuccessViewSet, TutorialViewSet, ConsultancyViewset, AccessToFinanceViewset, RegisterUser

router = DefaultRouter()
router.register('news', NewsViewSet)
router.register('service', OurServiceViewSet)
router.register('success', OurSuccessViewSet)
router.register('tutorials', TutorialViewSet)
router.register('consultancy', ConsultancyViewset)
router.register('finance', AccessToFinanceViewset)






urlpatterns = [
    path('', include(router.urls)),
    path('registration/', RegisterUser.as_view(), name='register-user'),
]