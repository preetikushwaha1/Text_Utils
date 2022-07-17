from django.urls import path
from accounts import views

urlpatterns =[
    path('index', views.index_fun, name= "index"),
    path('register', views.register_fun, name="register" ),
    path('login', views.login_fun, name="login"),
    path('logout', views.logout_fun, name="logout"),
    path('text_utils', views.text_utils_func, name="Text_Utils"),
    

]