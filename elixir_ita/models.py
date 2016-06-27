from django.db import models
from django.utils import timezone
from datetime import date


# Create your models here.

class Course(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=400, null=True)
    code = models.CharField(max_length=20, null=True)
    venue = models.CharField(max_length=200, null=True)
    data = models.CharField(max_length=100, null=True)
    deadline = models.CharField(max_length=100, null=True, blank=True)
    acceptance = models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField(blank=True)
    #I need a date to compare with date.today() - see method is_past_true
    course_date = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    year = models.CharField(max_length=4, null=True)

    def is_past_due(self):
        if date.today() < self.course_date:
            return True
        return False
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Trainer(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200, null=True)
    code = models.CharField(max_length=80, primary_key=True, null=False)
    keywords = models.CharField(max_length=400, null=True, blank=True)
    bio = models.TextField(blank=True)
    affiliation = models.CharField(max_length=400, null=True, blank=True)
    photo = models.CharField(max_length=80, null=True, blank=True)
    contact = models.CharField(max_length=400, null=True, blank=True)
    website = models.CharField(max_length=400, null=True, blank=True)
    course_teach = models.TextField(blank=True)
    course_organise = models.TextField(blank=True)

    def __str__(self):
        return self.name

