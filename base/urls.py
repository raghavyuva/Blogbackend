from django.urls import path
from base import views
from .views import Blog_list, UserList, UserLogin
urlpatterns = [
    path("blog", Blog_list),
    path("user", UserList),
    path("login", UserLogin)
]
