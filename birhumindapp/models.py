from django.db import models
from django.contrib.auth.models import User



class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title
class UserProfile(models.Model):
    username = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    education_level = models.CharField(max_length=20, choices=[
        ('no-formal', 'No Formal Education'),
        ('primary', 'Primary'),
        ('secondary', 'Secondary'),
        ('degree', 'Degree'),
        ('masterPlus', 'Masters or Higher')
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

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
    company_logo = models.ImageField(upload_to='finance_logo/', blank=True, null=True)
    description=models.TextField()
    url=models.URLField()
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

class Tutorial_Instructor(models.Model):
    instructor_name = models.CharField(max_length=100)
    instructor_image=models.ImageField(upload_to='instructor_images/', blank=True, null=True)
    instructor_title=models.CharField(max_length=200)
    about_instructor=models.TextField()

class Tutorial(models.Model):
    title = models.CharField(max_length=200)
    course_image = models.ImageField(upload_to='tutorials_images/', blank=True, null=True)
    description = models.TextField()
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title



class DocumentSubmission(models.Model):
    name = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    selected_documents = models.JSONField()  # Stores the selected documents
    selected_templates = models.JSONField(default=list)  # Stores the selected templates
    created_at = models.DateTimeField(auto_now_add=True)
    education_level = models.CharField(
        max_length=20,
        choices=[
            ('no-formal', 'No Formal Education'),
            ('primary', 'Primary'),
            ('secondary', 'Secondary'),
            ('degree', 'Degree'),
            ('masterPlus', 'Masters or Higher')
        ]
    )
    document_type = models.CharField(
        max_length=20,
       
        choices=[
            ('bds', 'Bds Document'),
            ('business', 'Business'),
            ('tutorial', 'Tutorial')
        ]
    )

    def __str__(self):
        return f"Document Submission: {self.name} - {self.institution}"

