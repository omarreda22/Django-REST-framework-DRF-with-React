from django.urls import path

from .views import (
	PostListCreate,
	PostDetailsDelete,
)

app_name = 'blog_api'


urlpatterns = [
	path('', PostListCreate.as_view(), name='listcreate'),
	path('<int:pk>/', PostDetailsDelete.as_view(), name='detailsdelete')
]