from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import News, Category, Tag

admin.site.register(News)
admin.site.register(Category)
admin.site.register(Tag)
