import io

from django.conf import settings
from django.contrib import admin
from rest_framework.exceptions import ValidationError
from vws import VWS
from vws.exceptions import TargetStatusProcessing

from .models import ARContents

admin.site.site_header = 'SMIT AR/VR 제작 기술'
admin.site.site_title = '201831005 김여진'
admin.site.index_title = 'AR Contents Management System'


@admin.register(ARContents)
class ARContentsAdmin(admin.ModelAdmin):

	list_display = ['id', 'name', 'image_contents', 'image_target', 'description']
	fields = ['name', 'image_contents', 'image_target', 'description']

	vws_client = VWS(
		server_access_key=settings.VWS_SERVER_ACCESS_KEY,
		server_secret_key=settings.VWS_SERVER_SECRET_KEY,
	)

	def save_model(self, request, obj, form, change):
		obj.save()

		if 'name' in form.changed_data:
			try:
				image_target_path = form.cleaned_data['image_target'].name.split('/')[-1]
				with open(f'./media/targets/{image_target_path}', 'rb') as my_image_file:
					my_image = io.BytesIO(my_image_file.read())

				target_id = self.vws_client.add_target(
					name=form.cleaned_data['name'],
					width=1,
					image=my_image,
					active_flag=True,
					application_metadata=None,
				)
			except Exception as e:
				raise ValidationError(str(e))
			else:
				obj.target_id = target_id
				obj.save()

		return

	def delete_model(self, request, obj):
		try:
			self.vws_client.delete_target(obj.target_id)
		except TargetStatusProcessing:
			raise ValidationError('뷰포리아에서 이미지 처리 중입니다. 잠시 후 다시 시도해주세요.')
		else:
			super().delete_model(request, obj)

		return

	def delete_queryset(self, request, queryset):
		try:
			for contents in queryset:
				self.vws_client.delete_target(contents.target_id)
		except TargetStatusProcessing:
			raise ValidationError('뷰포리아에서 이미지 처리 중입니다. 잠시 후 다시 시도해주세요.')
		else:
			queryset.delete()

		return
