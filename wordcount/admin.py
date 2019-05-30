from django.contrib import admin
from .models import Blog

# Register your models here.
admin.site.register(Blog) #django에 있는 admin.site에 Blog라는 model 등록