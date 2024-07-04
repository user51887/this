from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    
    path('<int:id>' , views.service_detail , name='service_detail'),
]
