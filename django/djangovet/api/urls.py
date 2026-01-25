from django.contrib import admin
from django.urls import path
# from . import views
from .views import RoomView, CreateRoomView

urlpatterns = [
    # path('', views.main),
    path('room', RoomView.as_view()),
    path('create-room', CreateRoomView.as_view())

]
