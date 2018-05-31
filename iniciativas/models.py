from django.db import models
from django import forms
from django.conf import settings

class Image(models.Model):
    title = models.CharField(max_length=100, default='0000000', editable=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d', default='settings.MEDIA_ROOT/default.jpg')
    datestamp = models.DateTimeField(auto_now_add=True)
    upload_by = models.ForeignKey('auth.User', related_name='uploaded_documents', on_delete=models.CASCADE)

class Community_issue(models.Model):
    name = models.CharField(max_length=100, default='0', editable=True)
    description = models.TextField()
    image = models.ForeignKey(Image,on_delete=models.CASCADE, default=0)
    def __str__(self):
        return self.name

class Community_issue_attribute(models.Model):
    Community_issue = models.ForeignKey(Community_issue, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default='0', editable=True)
    value_type = models.CharField(max_length=30, blank=True)
    value = models.TextField()
    def __str__(self):
        return self.name

