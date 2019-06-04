from django.urls import include, path

from . import views

urlpatterns = [
    # user site
    path('api/user/', views.UserListCreate.as_view()),
    path('api/user/<int:pk>/', views.UserDetail.as_view()),
    path('api/user/<int:pk>/update/', views.UserUpdate.as_view()),
    path('api/user/<int:pk>/delete/', views.UserDelete.as_view()),

    # order site
    path('api/order/', views.OrderListCreate.as_view()),
    path('api/order/<int:pk>/', views.OrderDetail.as_view()),
    path('api/order/<int:pk>/update/', views.OrderUpdate.as_view()),
    path('api/order/<int:pk>/delete/', views.OrderDelete.as_view()),
    path('api/order/<int:pk>/<int:owner_id>/', views.UserOrderDetail.as_view()),
]