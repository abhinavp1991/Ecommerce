from django.urls import path,include
from rest_framework.authtoken import views
from .views import home

urlpatterns =[
    path('',home,name='api.home'),
    path('category/', include('api_management.category.urls')),
    path('product/',include('api_management.product.urls')),
    path('user/',include('api_management.user.urls')),
    path('order/',include('api_management.order.urls')),
    path('payment/',include('api_management.payment.urls')),
    path('api-token-auth/',views.obtain_auth_token,name='api_token_auth'),
]