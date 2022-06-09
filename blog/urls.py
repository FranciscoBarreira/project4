from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('upvote/<slug:slug>/', views.Upvote.as_view(), name='blog_upvote'),
    path('downvote/<slug:slug>/', views.Downvote.as_view(), name='blog_downvote'),
    path('search', views.SearchPost.as_view(), name='search'),
]