from django.contrib import admin
from .models import *




class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id','full_name', 'bio', 'image']


    search_fields = ("full_name","bio")
    ordering = ("created_at",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']


    search_fields = ("name",)
    ordering = ("created_at",)



class BookAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'body', 'image', 'price', 'category', 'author']


    search_fields = ("name","price")
    ordering = ("created_at",)





admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
