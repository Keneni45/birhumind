from django.db import models
from django.contrib.auth.models import User
class Topic(models.Model):
    top_name = models.CharField(max_length=100)
    # description = models.TextField()

    def __str__(self):
         return self.top_name
class WebPage(models.Model):
    topic=models.ForeignKey(Topic, on_delete=models.CASCADE)
    name=models.CharField(max_length=120)
    # url=models.URLField(unique=True)

    def __str__(self):
        return self.name
class AccessRecord(models.Model):
    title=models.ForeignKey(WebPage, on_delete=models.CASCADE)
    date=models.DateField()
    logo = models.ImageField(upload_to='finance_images/', blank=True, null=True)

    def __str__(self):
      return (self.title)

class OurSuccess(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    student_number=models.CharField(max_length=50)
    total_success=models.CharField(max_length=50)
    chief_expert=models.CharField(max_length=50)
    years_experience=models.CharField(max_length=50)

    def __str__(self):
        return self.title
class AccessToFinance(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
class Consultancy(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title


class OurService(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=200)
    subHead = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    category = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['-published_date']  # Newest articles first

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    education_level = models.CharField(max_length=100, choices=[('No Formal Education', 'No Formal Education'),('Primary Education','Primary Education'),('Secondary Education','Secondary Education'),('Degree','Degree'), ('Master Degree','Master Degree')])

    def __str__(self):
        return self.user.username

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    subHead = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    category = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['-published_date']  # Newest articles first

    def __str__(self):
        return self.title

    
class Tutorial(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='tutorials_images/', blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=100)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title




# Create your models here.