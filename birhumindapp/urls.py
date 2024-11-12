from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import submit_document, NewsViewSet, OurServiceViewSet,Tutorial_InstructorViewset,  OurSuccessViewSet, TutorialViewSet, ConsultancyViewset, AccessToFinanceViewset, RegisterUser
from . import views
router = DefaultRouter()
router.register('news', NewsViewSet)
router.register('service', OurServiceViewSet)
router.register('success', OurSuccessViewSet)
router.register('tutorials', TutorialViewSet)
router.register('consultancy', ConsultancyViewset)
router.register('finance', AccessToFinanceViewset)
router.register('instructor', Tutorial_InstructorViewset)
#router.register('submit', submit_document)






urlpatterns = [
    path('', include(router.urls)),
    path('registration/', RegisterUser.as_view(), name='register-user'),
    #path('submit/', views.submit_document, name='submit_document'),
    
]


# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import (
#     submit_document, 
#     NewsViewSet, 
#     OurServiceViewSet, 
#     Tutorial_InstructorViewset,  
#     OurSuccessViewSet, 
#     TutorialViewSet, 
#     ConsultancyViewset, 
#     AccessToFinanceViewset, 
#     RegisterUser
# )
# from . import views

# # Registering viewsets with the DefaultRouter
# router = DefaultRouter()
# router.register('news', NewsViewSet)
# router.register('service', OurServiceViewSet)
# router.register('success', OurSuccessViewSet)
# router.register('tutorials', TutorialViewSet)
# router.register('consultancy', ConsultancyViewset)
# router.register('finance', AccessToFinanceViewset)
# router.register('instructor', Tutorial_InstructorViewset)

# urlpatterns = [
#     # Include the router URLs
#     path('', include(router.urls)),
    
#     # Define additional API endpoints
#     path('registration/', RegisterUser.as_view(), name='register-user'),
#     path('submit', views.submit_document, name='submit_document'),  # This is the form submission endpoint
# ]
