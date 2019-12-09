from django.urls import path

from .views import DownloadView, MarkerListView

app_name = 'contents'

urlpatterns = [
	path('markers', MarkerListView.as_view(), name='markers'),
	path('images/<str:marker>', DownloadView.as_view(), name='download')
]
