from django.urls import path
from . import views

urlpatterns = [
    path('',views.Route.as_view()),
    path('users/', views.AccountList.as_view()),
]
