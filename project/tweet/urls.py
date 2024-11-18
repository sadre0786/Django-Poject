from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.tweet_list, name='tweet_list'),
    path('tweet_create/',views.tweet_create, name='tweet_create'),
    path('<int:tweet_id>/tweet_delete/',views.tweet_delete, name='tweet_delete'),
    path('<int:tweet_id>/tweet_edit',views.tweet_edit, name='tweet_edit'),
    path('register/',views.register, name='registration'),
    path('search/',views.search, name='search'),
    
    
]
