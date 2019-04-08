from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('landing/', views.landingpage, name='landingpage'),
    path('scoring/', views.scoringpage, name='scoringpage'),
    path('round1/', views.rd1holelist.as_view(), name='rd1holelist'),
    path('round1/<int:pk>', views.rd1holedetail, name='rd1holedetail'),
    path('round1/leaderboard', views.rd1leaderboard, name='rd1leaderboard'),
    path('entertips/', views.entertips, name='entertips'),

]
