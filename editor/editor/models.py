from django.db import models
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    author = models.ForeignKey('auth.User')
    project_name = models.CharField(max_length=200)
    project_description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    last_modified_date = models.DateTimeField(blank=True, null=True)

    def save_project(self):
        self.last_modified_date = timezone.now()
        self.save()

    def __str__(self):
        return self.project_name
