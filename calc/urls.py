from django.urls import path
from calc import views

urlpatterns =[

        path('', views.hello,name='Home'),
        path('add',views.addition),
]