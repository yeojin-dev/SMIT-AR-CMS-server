from django.contrib import admin

from .models import ARContents

admin.site.site_header = 'SMIT AR/VR 제작 기술'
admin.site.site_title = '201831005 김여진'
admin.site.index_title = 'AR Contents Management System'


@admin.register(ARContents)
class ARContentsAdmin(admin.ModelAdmin):
	list_display = ['id', 'image', 'marker', 'description']
