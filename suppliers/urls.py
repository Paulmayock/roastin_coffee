from django.urls import path
from . import views

urlpatterns = [
    path('', views.SupplierList.as_view(), name='suppliers'),
]
