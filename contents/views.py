from rest_framework import generics
from rest_framework.response import Response

from .models import ARContents
from .serializers import ARContentsSerializer, ARMarkersSerializer


class MarkerListView(generics.GenericAPIView):
	serializer_class = ARMarkersSerializer
	queryset = ARContents.objects.all()

	def get(self, request):
		serializer = self.get_serializer(self.get_queryset(), many=True)
		return Response({'results': serializer.data})


class DownloadView(generics.RetrieveAPIView):
	serializer_class = ARContentsSerializer
	queryset = ARContents.objects.all()
	lookup_field = 'name'
