from django.db import models
from django_extensions.db.models import TimeStampedModel


class ARContents(TimeStampedModel):
	image_contents = models.ImageField(upload_to='contents')
	image_target = models.ImageField(upload_to='targets', help_text='JPG 파일만 사용해주세요.')
	target_id = models.CharField(max_length=255, blank=True)
	name = models.CharField(max_length=64)
	description = models.CharField(max_length=255, blank=True, null=True)

	class Meta:
		db_table = 'ar_contents'
		verbose_name = 'AR Content'

	def __str__(self):
		return self.image_contents.name
