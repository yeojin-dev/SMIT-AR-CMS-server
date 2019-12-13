from django.urls import path

from .views import DownloadView, MarkerListView

app_name = 'contents'

urlpatterns = [
	path('', MarkerListView.as_view(), name='markers'),
	path('<str:name>', DownloadView.as_view(), name='download')
]
