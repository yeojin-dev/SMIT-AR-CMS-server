from rest_framework.generics import RetrieveAPIView

from .models import ARContents
from .serializers import ARContentsSerializer


class DownloadView(RetrieveAPIView):
	serializer_class = ARContentsSerializer
	queryset = ARContents.objects.all()
	lookup_field = 'marker'
