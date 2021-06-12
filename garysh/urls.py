from django.urls import path
from .views import *

app_name = "garysh"
urlpatterns = [
    path('', index, name="index"),
    path('login/', loginUser, name="login"),
    path('register/', registerView.as_view(), name="registration"),
    path('logout/', logoutUser, name="logout"),
    path('delete/<int:id>', deleteUser, name="delete"),
    path('edit/<slug:pk>', UserUpdateView.as_view(), name="edit"),
]
