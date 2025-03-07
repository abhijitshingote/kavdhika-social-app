from django.urls import path
from . import views

app_name = 'kavdhika_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/create/', views.create_post, name='create_post'),
    path('post/<int:post_id>/react/', views.react_to_post, name='react_to_post'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]