from django.urls import path
from cyblog.views import login_view, logout_view
from . import views


urlpatterns= [
    path('cyblog/login/',login_view),
    path('cyblog/logout/',logout_view),
    path('create_user/',views.create_user,name='create_user'),
    path('post_list/',views.post_list,name='post_list'),
    path('create_post/(\w+)/',views.create_post, name='create_post'),
    path('search_post/',views.search_post, name='search_post')
]
