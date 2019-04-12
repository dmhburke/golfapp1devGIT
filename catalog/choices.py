from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Sum, Count
from django.views import generic

#CHOICES
YES_NO = (
    ("YES", "Yes"),
    ("NO", "No"),
    )

DAYS = (
    ("FRIDAY", "Friday"),
    ("SATURDAY", "Saturday"),
    ("SUNDAY", "Sunday"),
    )

#TIPPING INPUT
GAME_1 = (
    ("", "Lowest score Friday"),
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
    ("PACERS", "Pacers"),
    ("CELTICS", "Celtics"),
    )

GAME_4 = (
    ("", "Select results"),
    ("NUGGETS", "Nuggets"),
    ("SPURS", "Spurs"),
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

#RESULTS CHECK - change empty result value
GAME_1R = (
    ("NOT_COMPLETE", "No result"),
    ("PLAYER_1", "Player 1"),
    ("PLAYER_2", "Player 2"),
    ("TIED", "Tied"),
    )

GAME_2R = (
    ("NOT_COMPLETE", "No result"),
    ("GIANTS", "Giants"),
    ("PIRATES", "Pirates"),
    )

GAME_3R = (
    ("NOT_COMPLETE", "No result"),
    ("PACERS", "Pacers"),
    ("CELTICS", "Celtics"),
    )

GAME_4R = (
    ("NOT_COMPLETE", "No result"),
    ("NUGGETS", "Nuggets"),
    ("SPURS", "Spurs"),
    )

GAME_5R = (
    ("NOT_COMPLETE", "No result"),
    ("MAPLE_LEAFS", "Maple Leafs"),
    ("BRUINS", "Bruins"),
    )

GAME_6R = (
    ("NOT_COMPLETE", "No result"),
    ("ROYALS", "Player 1"),
    ("INDIANS", "Player 2"),
    ("TIED", "Tied"),
    )

GAME_7R = (
    ("NOT_COMPLETE", "No result"),
    ("MAN_CITY", "Man City"),
    ("TOTTENHAM", "Tottenham"),
    ("DRAW", "Draw"),
    )

GAME_8R = (
    ("NOT_COMPLETE", "No result"),
    ("WEST_HAM", "West Ham"),
    ("LEICESTER_CITY", "Leicester City"),
    ("DRAW", "Draw"),
    )

GAME_9R = (
    ("NOT_COMPLETE", "No result"),
    ("YANKEES", "Yankees"),
    ("ROYALS", "Royals"),
    )

GAME_10R = (
    ("NOT_COMPLETE", "No result"),
    ("ISLANDERS", "Islanders"),
    ("PENGUINS", "Penguins"),
    )
