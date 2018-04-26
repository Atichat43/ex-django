from django.urls import re_path
from my_app import views

urlpatterns = [
    re_path(r'^$',views.PostListView.as_view(),name='post_list'),
    re_path(r'^about/$',views.AboutView.as_view(),name='about'),
    re_path(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
]
