from django.conf.urls import url
from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.allArticle , name='allArticle'),
    path('<int:pk>/<slug:slug>/', views.articleDtails , name='articleDtails'),

]

