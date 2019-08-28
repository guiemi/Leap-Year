from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('', views.after_century, name='after_century',
    )
]

