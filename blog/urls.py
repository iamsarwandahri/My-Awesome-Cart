from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='blog'),
    path('<int:id>/blogpost/',views.blogpost,name='blogpost')
]
