from django.urls import include, path

from . import views

urlpatterns = [
    path('api/user/', views.UserListCreate.as_view()),
]