from django.urls import path, include

from . import views


app_name = 'apps'

urlpatterns = [
    path('', views.home, name="home"),
    path('posts/', views.posts, name="posts"),
    path('post/<int:post_id>/', views.post, name="post"),
    path('new_post/', views.new_post, name="new_post"),
    path('add_body/<int:post_id>/', views.add_body, name="add_body"),
    path('edit_body/<int:body_id>/', views.edit_body, name="edit_body"),
    path('delete_post/<int:post_id>/', views.delete_post, name="delete_post")
]
