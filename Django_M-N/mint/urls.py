from django.urls import path
from . import views

app_name = 'mint'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('create/', views.create, name = 'create'),
    path('<int:article_pk>/', views.detail, name = 'detail'),
    path('<int:article_pk>/comments/create/', views.comment_create, name = 'comment_create'), # 댓글생성
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    path('<int:article_pk>/likes/', views.likes, name='likes'),# 좋아요
   
]
