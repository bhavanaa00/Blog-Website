from . import views
from django.urls import path

urlpatterns = [
  path('', views.PostList.as_view(),name='home'),
  path('contact/', views.contact, name='contact'),
  path('posts/', views.AllPost.as_view(), name='posts'),
  path('subscribe/', views.News, name='subscribe'),
  path('<slug:slug>/', views.DetailView.as_view(), name="post_detail")
  
]