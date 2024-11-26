from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import News, OurService, Event, Subscription,  OurSuccess, Tutorial, Consultancy, AccessToFinance,  Tutorial_Instructor
from .serializers import EventSerializer, SubscriptionSerializer,  DocumentSubmissionSerializer, NewsSerializer, OurServiceSerializer,  OurSuccessSerializer, TutorialSerializer, ConsultancySerializer, AccessToFinanceSerializer, UserProfileSerializer, Tutorial_InstructorSerializer
from .utils import send_subscription_email
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.http import Http404
class EventListCreateView(APIView):
   
    def get(self, request):
        # Get all events and return them as a list
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Create a new event
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the new event to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Admin view to list all users

@login_required
def view_users(request):
    if not request.user.is_staff:
        raise Http404("You are not authorized to view this page.")
    
    users = UserProfile.objects.all()
    return render(request, 'users/admin_users.html', {'users': users})

# Approve user registration
@login_required
def approve_user(request, user_id):
    if not request.user.is_staff:
        raise Http404("You are not authorized to perform this action.")
    
    user = UserProfile.objects.get(id=user_id)
    if user:
        user.approval_status = 'approved'
        user.save()
        messages.success(request, f"User {user.username} approved successfully.")
    return redirect('users:view_users')

# Deny user registration
@login_required
def deny_user(request, user_id):
    if not request.user.is_staff:
        raise Http404("You are not authorized to perform this action.")
    
    user = UserProfile.objects.get(id=user_id)
    if user:
        user.approval_status = 'denied'
        user.save()
        messages.success(request, f"User {user.username} denied successfully.")
    return redirect('users:view_users')

# Delete a user account
@login_required
def delete_user(request, user_id):
    if not request.user.is_staff:
        raise Http404("You are not authorized to perform this action.")
    
    user = UserProfile.objects.get(id=user_id)
    if user:
        user.delete()
        messages.success(request, f"User {user.username} deleted successfully.")
    return redirect('users:view_users')



@api_view(['POST'])
def subscribe(request):
    if request.method == 'POST':
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            # Check if email already exists
            if Subscription.objects.filter(email=email).exists():
                return Response({'message': 'This email is already subscribed.'}, status=status.HTTP_400_BAD_REQUEST)
            
            # Save the subscription
            serializer.save()
            
            # Send confirmation email
            send_subscription_email(email)
            
            return Response({'message': 'Subscription successful!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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

