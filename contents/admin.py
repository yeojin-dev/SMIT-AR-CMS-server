from django.contrib import admin

from .models import ARContents


@admin.register(ARContents)
class ARContentsAdmin(admin.ModelAdmin):
	list_display = ['id', 'image', 'marker', 'description']
