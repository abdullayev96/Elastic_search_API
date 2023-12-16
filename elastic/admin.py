from django.contrib import admin
from .models import ElasticDemo



class ElasticDemoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']
    search_fields = ['title']


admin.site.register(ElasticDemo, ElasticDemoAdmin)
