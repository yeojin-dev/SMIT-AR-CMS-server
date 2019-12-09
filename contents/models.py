from django.db import models
from django_extensions.db.models import TimeStampedModel


class ARContents(TimeStampedModel):
	image = models.ImageField()
	marker = models.CharField(max_length=30, unique=True, db_index=True)
	description = models.CharField(max_length=255, blank=True, null=True)

	class Meta:
		db_table = 'ar_contents'
		verbose_name = 'AR Content'

	def __str__(self):
		return self.image.name
