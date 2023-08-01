from django.urls import path
from accounts.views import *


urlpatterns = [
    path('login/',login_page,name="login_page"),
    path('register/',signup,name='signup'),
    path('activate/<email_token>',activate_email,name="activate_email")
]