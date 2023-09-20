from django.contrib import admin
from .models import Category, Products

admin.site.register(Category)


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    raw_id_fields = ('category',)
