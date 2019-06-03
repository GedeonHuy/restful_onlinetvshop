from django.urls import include, path

from . import views

urlpatterns = [
    path('api/user/', views.UserListCreate.as_view()),
    path('api/user/<int:pk>/', views.UserDetail.as_view()),
    path('api/user/<int:pk>/update/', views.UserUpdate.as_view()),
    path('api/user/<int:pk>/delete/', views.UserDelete.as_view()),
]