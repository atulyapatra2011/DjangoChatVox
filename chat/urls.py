from django.urls import path
from . import views

urlpatterns = [
    path('',views.ChatVox_Login,name='login'),
    path('Home/',views.home_Chat,name='home'),
    path('<str:room>/', views.room, name='room'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('logout/',views.logout_view,name='logout'),





    # path('<str:room>/', views.room, name='room'),
    # path('Home/checkview', views.checkview, name='checkview'),
    # path('send', views.send, name='send'),
    # path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]