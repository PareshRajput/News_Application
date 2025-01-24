from django.urls import path

from . import views 
urlpatterns = [    
    path('', views.index, name='index'),
    # path('news/', views.news, name='news'),
    # path('news/<int:news_id>/', views.news_detail, name='news_detail'),
    # path('news/<int:news_id>/edit/', views.edit_news, name='edit_news'),
    # path('news/<int:news_id>/delete/', views.delete_news, name='delete_news'),
    # path('news/add/', views.add_news, name='add_news'),
]