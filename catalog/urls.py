from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('landing/', views.landingpage, name='landingpage'),
    path('leaderboard/',views.fullleaderboard, name='fullleaderboard'),
    path('scoring/', views.scoringpage, name='scoringpage'),
    path('topgolf/', views.topgolf, name='topgolf'),
    path('racing/', views.racing, name='racing'),
    path('entertips/', views.entertips, name='entertips'),
    path('tipresults/', views.tipresults, name='tipresults'),
    path('entersocial/', views.entersocial, name='entersocial'),
    path('tourdetails/', views.tourdetails, name='tourdetails'),
    path('touragenda/', views.touragenda, name='touragenda'),
    path('tourmap/', views.tourmap, name='tourmap'),
    path('tourplayers/', views.tourplayers, name='tourplayers'),
    path('round1/', views.rd1holelist.as_view(), name='rd1holelist'),
    path('round1/<int:pk>', views.rd1holedetail, name='rd1holedetail'),
    path('round1/leaderboard', views.rd1leaderboard, name='rd1leaderboard'),
    path('round2/', views.rd2holelist.as_view(), name='rd2holelist'),
    path('round2/<int:pk>', views.rd2holedetail, name='rd2holedetail'),
    path('round2/leaderboard', views.rd2leaderboard, name='rd2leaderboard'),
    path('round3/', views.rd3holelist.as_view(), name='rd3holelist'),
    path('round3/<int:pk>', views.rd3holedetail, name='rd3holedetail'),
    path('round3/leaderboard', views.rd3leaderboard, name='rd3leaderboard'),
]
