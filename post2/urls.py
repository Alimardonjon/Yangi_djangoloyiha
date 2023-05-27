from django.urls import path
from .views import Ali
urlpatterns=[
    path('fay/',Ali.as_view(), name='home3')
  ]