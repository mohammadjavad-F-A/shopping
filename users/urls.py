from django.urls import path
from .views import *

urlpatterns = [

    path('login/', login_user, name='login'),
    path('signin/', signin, name='signin'),
    path('forgot/', forgot, name='forgot'),
    path('profile/', profile, name='profile'),
    path('logout/', logout_user, name='logout'),
    path('more_user/', more_user, name='more_user'),
]