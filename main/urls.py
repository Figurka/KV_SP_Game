from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('signup/', views.signup, name="signup"),
    path('accounts/', include("allauth.urls"))
]