from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Sum, Count
from django.views import generic

#CHOICES
YES_NO = (
    ("YES", "Yes"),
    ("NO", "No"),
    )

GAME_1 = (
    ("", "Select result"),
    ("PLAYER_1", "Player 1"),
    ("PLAYER_2", "Player 2"),
    ("TIED", "Tied"),
    )

GAME_2 = (
    ("", "Select result"),
    ("GIANTS", "Giants"),
    ("PIRATES", "Pirates"),
    )

GAME_3 = (
    ("", "Select result"),
    ("TEAM_1", "Player 1"),
    ("TEAM_2", "Player 2"),
    )

GAME_4 = (
    ("", "Select result"),
    ("TEAM_1", "Player 1"),
    ("TEAM_2", "Player 2"),
    )

GAME_5 = (
    ("", "Select result"),
    ("MAPLE_LEAFS", "Maple Leafs"),
    ("BRUINS", "Bruins"),
    )

GAME_6 = (
    ("", "Select result"),
    ("ROYALS", "Player 1"),
    ("INDIANS", "Player 2"),
    ("TIED", "Tied"),
    )

GAME_7 = (
    ("", "Select result"),
    ("MAN_CITY", "Man City"),
    ("TOTTENHAM", "Tottenham"),
    ("DRAW", "Draw"),
    )

GAME_8 = (
    ("", "Select result"),
    ("WEST_HAM", "West Ham"),
    ("LEICESTER_CITY", "Leicester City"),
    ("DRAW", "Draw"),
    )

GAME_9 = (
    ("", "Select result"),
    ("YANKEES", "Yankees"),
    ("ROYALS", "Royals"),
    )

GAME_10 = (
    ("", "Select result"),
    ("ISLANDERS", "Islanders"),
    ("PENGUINS", "Penguins"),
    )
