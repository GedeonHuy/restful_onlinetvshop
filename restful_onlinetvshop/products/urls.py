from django.urls import include, path

from . import views

urlpatterns = [
    #test-start
    path('product/<str:pk>/', views.Detail.as_view()),
    #test-end

    path('api/product/', views.ProductListCreate.as_view()),
    path('api/product/<str:pk>/', views.ProductDetail.as_view()),
    path('api/product/<str:pk>/update/', views.ProductUpdate.as_view()),
    path('api/product/<str:pk>/delete/', views.ProductDelete.as_view()),
]