from django.contrib import admin
from birhumindapp.models import Subscription, DocumentSubmission, Tutorial_Instructor, UserProfile,  News, OurService,OurSuccess, Tutorial, Consultancy, AccessToFinance

class DocumentRequestAdmin(admin.ModelAdmin):
    readonly_fields=('name', 'institution', 'education_level', 'document_type', 'selected_documents', 'selected_templates')
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
# class UserProfileAdmin(admin.ModelAdmin):
    
#     readonly_fields = ('username', 'age', 'gender', 'education_level', 'created_at')
    
#     def has_add_permission(self, request):
#         return False

#     def has_change_permission(self, request, obj=None):
#         return False

#     def has_delete_permission(self, request, obj=None):
#         return False
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'age', 'gender', 'education_level', 'approval_status', 'created_at')
    list_filter = ('approval_status',)
    search_fields = ('username', 'email')
class SubscriptionAdmin(admin.ModelAdmin):

    list_display = ('email', 'subscribed_at')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False 

# Register the Subscription model with the admin site
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(DocumentSubmission, DocumentRequestAdmin)    
admin.site.register(News)
admin.site.register(OurService)
admin.site.register(OurSuccess)
admin.site.register(Tutorial)
admin.site.register(Consultancy)
admin.site.register(AccessToFinance)
admin.site.register(Tutorial_Instructor)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.site_header = "Birhuminds Admin Interface"
admin.site.index_title = "Welcome to My Admin Portal"



class TutorialInstructor(admin.ModelAdmin):
    list_display=('instructor_name', 'instructor_image', 'instructor_title', 'about_instructor')
class AccessToFinanceAdmin(admin.ModelAdmin):
    list_display=('title', 'description', 'image')
class ConsultancyAdmin(admin.ModelAdmin):
    list_display=('title', 'description')
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title','subHead', 'author', 'published_date', 'category')
    search_fields = ('title', 'author', 'category')
    list_filter = ('category',)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','subHead', 'author', 'published_date', 'category')
    search_fields = ('title', 'author', 'category')
    list_filter = ('category',)

class TutorialAdmin(admin.ModelAdmin):
    list_display = ('title','subHead', 'author', 'published_date', 'category')
    search_fields = ('title', 'author', 'category')
    list_filter = ('category',)

class OurServiceAdmin(admin.ModelAdmin):
    list_display=('title', 'description')
class OurSuccessAdmin(admin.ModelAdmin):
    list_display=('title', 'description', 'student_number', 'total_success', 'chief_expert', 'years_experience')

