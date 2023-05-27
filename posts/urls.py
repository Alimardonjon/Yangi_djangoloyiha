from django.urls import path
from .views import Alimardon,Fayozbek
urlpatterns=[
    path('',Alimardon.as_view(), name='home'),
    path('fayoz/',Fayozbek.as_view(),name='home2')

]