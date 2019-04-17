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
    ("", "RBC low thru Fri"),
    ("PLAYER_1", "Jordan Spieth"),
    ("PLAYER_2", "Dustin Johnson"),
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
    ("", "Select result"),
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
    ("ROYALS", "Royals"),
    ("INDIANS", "Indians"),
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
    ("KANSAS_CITY", "Kansas City"),
    )

GAME_10 = (
    ("", "Select result"),
    ("HURRICANES", "Hurricanes"),
    ("CAPITALS", "Capitals"),
    )

#RESULTS CHECK - change empty result value
GAME_1R = (
    ("NOT_COMPLETE", "No result"),
    ("PLAYER_1", "Jordan Spieth"),
    ("PLAYER_2", "Dustin Johnson"),
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
    ("ROYALS", "Royals"),
    ("INDIANS", "Indians"),
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
    ("KANSAS_CITY", "Kansas City"),
    )

GAME_10R = (
    ("NOT_COMPLETE", "No result"),
    ("HURRICANES", "Hurricanes"),
    ("CAPITALS", "Capitals"),
    )
