
from django.urls import path
from . import views
from .views import MessageListView

urlpatterns = [
    path('', views.index, name='index'),
    path('messages/', MessageListView.as_view(), name='message-list'),
]
