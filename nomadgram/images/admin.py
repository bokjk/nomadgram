from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    
    list_display_links = (
        'location',
    )

    search_fields = (
        'location',
        'caption',
    )

    list_filter = (
        'location',
        'creator',
    )

    list_display = (
        'created_at',
        'updated_at',
        'file',
        'location',
        'caption',
        'creator',
    )

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = (
        'image',
        'created_at',
        'updated_at',
        'creator',
    )

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    
    list_display = (
        'created_at',
        'updated_at',
        'message',
        'creator',
        'image',
    )