from django.urls import path,include
from gas_service import views
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.ServiceRequestListView.as_view(), name='request_list'),
    path('request/', views.ServiceRequestCreateView.as_view(), name='request_create'),
    
]