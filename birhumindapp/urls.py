from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import  DocumentSubmissionView, NewsViewSet, OurServiceViewSet,Tutorial_InstructorViewset,  OurSuccessViewSet, TutorialViewSet, ConsultancyViewset, AccessToFinanceViewset, RegisterUser
from . import views

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
    path('subscribe', views.subscribe, name='subscribe'),
    path('admin/users/', views.view_users, name='view_users'),
    path('admin/approve/<int:user_id>/', views.approve_user, name='approve_user'),
    path('admin/deny/<int:user_id>/', views.deny_user, name='deny_user'),
    path('admin/delete/<int:user_id>/', views.delete_user, name='delete_user')


]
