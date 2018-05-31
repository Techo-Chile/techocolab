from django.contrib import admin
from .models import Community_issue, Community_issue_attribute, Image

# Register your models here.
admin.site.register(Image)
admin.site.register(Community_issue)
admin.site.register(Community_issue_attribute)