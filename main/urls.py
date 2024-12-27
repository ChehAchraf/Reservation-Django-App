from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home , name ="home"),
    path('about/' , views.about , name ="about"),
    path('book/<int:activity_id>/', views.book_activity, name='book_activity'),

]