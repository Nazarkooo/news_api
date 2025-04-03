from django.contrib import admin

from .models import NewsType, NewsItem


admin.site.register(NewsType)
admin.site.register(NewsItem)