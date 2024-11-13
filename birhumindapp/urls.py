from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DocumentSubmissionView, NewsViewSet, OurServiceViewSet,Tutorial_InstructorViewset,  OurSuccessViewSet, TutorialViewSet, ConsultancyViewset, AccessToFinanceViewset, RegisterUser

router = DefaultRouter()
router.register('news', NewsViewSet)
router.register('service', OurServiceViewSet)
router.register('success', OurSuccessViewSet)
router.register('tutorials', TutorialViewSet)
router.register('consultancy', ConsultancyViewset)
router.register('finance', AccessToFinanceViewset)
router.register('instructor', Tutorial_InstructorViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('registration/', RegisterUser.as_view(), name='register-user'),
    path('submit/', DocumentSubmissionView.as_view(), name='submit-document'),

]
