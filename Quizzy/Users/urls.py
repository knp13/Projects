from django.urls import path
from Users.views import *

urlpatterns = [
    path('register/', register, name="register"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('profile/', profile_update, name="profile"),
    #path('profile/', profile, name="profile"),
]
