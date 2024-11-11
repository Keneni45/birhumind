from django.contrib import admin
from birhumindapp.models import WebPage, AccessRecord, Topic,  News, OurService,OurSuccess, Tutorial, Consultancy, AccessToFinance


admin.site.register(Topic)
admin.site.register(AccessRecord)
admin.site.register(WebPage)
admin.site.register(News)
admin.site.register(OurService)
admin.site.register(OurSuccess)
admin.site.register(Tutorial)
admin.site.register(Consultancy)
admin.site.register(AccessToFinance)
admin.site.site_header = "Birhuminds Admin Interface"
admin.site.index_title = "Welcome to My Admin Portal"# 


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

