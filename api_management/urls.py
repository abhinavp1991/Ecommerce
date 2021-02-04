from django.urls import path,include
from rest_framework.authtoken import views
from .views import home

urlpatterns =[
    path('',home,name='api.home'),
    path('category/', include('api_management.category.urls')),
    path('product/',include('api_management.product.urls')),
    path('user/',include('api_management.user.urls'))
]