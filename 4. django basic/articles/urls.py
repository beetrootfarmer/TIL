from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    # variable routing
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/comments/create/', views.comment_create, name='comment_create'),
    path('<int:article_pk>/delete/', views.delete, name='delete')
]