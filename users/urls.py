from django.urls import path
from users.views import register_view,logout_view,login_view




urlpatterns=[
     path("register/",register_view,name="signup"),
     path("login/",login_view,name="login"),
     path("logout/",logout_view,name="logout"),
    
     

]