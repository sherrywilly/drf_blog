from django.urls import path
app_name = 'blog_api'
from .views import PostList,PostDetail

urlpatterns = [
path('<int:pk>/',PostDetail.as_view(),name='detailcreate'),
path('',PostList.as_view(),name='listcreate')
]
