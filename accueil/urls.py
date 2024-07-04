from django.urls import path
from . import views

app_name = 'accueil'

urlpatterns = [
    path('',views.accueil, name='accueil' ),
    path('success/' , views.send_success , name='send_success')
    
]
