from django.urls import include, path

from . import views

urlpatterns = [
    path('api/brand/', views.BrandListCreate.as_view()),
    path('api/brand/<int:pk>/', views.BrandDetail.as_view()),
    path('api/brand/<int:pk>/update/', views.BrandUpdate.as_view()),
    path('api/brand/<int:pk>/delete/', views.BrandDelete.as_view()),
]
