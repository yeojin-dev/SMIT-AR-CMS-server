from django.urls import path

from .views import DownloadView

app_name = 'contents'

urlpatterns = [
	path('<str:marker>', DownloadView.as_view(), name='download')
]
