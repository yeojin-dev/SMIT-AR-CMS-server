from rest_framework import serializers

from .models import ARContents


class ARContentsSerializer(serializers.ModelSerializer):

	class Meta:
		model = ARContents
		fields = [
			'image',
			'marker',
		]


class ARMarkersSerializer(serializers.ModelSerializer):

	class Meta:
		model = ARContents
		fields = [
			'marker',
		]
