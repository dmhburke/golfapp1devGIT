from django.contrib import admin

# Register your models here.

from catalog.models import PlayerModel, Rd1HoleModel, Rd1SlotModel, Rd1ScoreModel, Rd1StablefordModel, Rd2HoleModel, Rd2SlotModel, Rd2ScoreModel, Rd2StablefordModel, Rd3HoleModel, Rd3SlotModel, Rd3ScoreModel, Rd3StablefordModel, EventEntryModel, LeaderBoardModel, SportsTippingModel, SportsTippingResultsModel, SportsTippingScoreModel, FridaySocialModel, SaturdaySocialModel, TourAgendaModel, TopGolfModel, RacingModel

# Define new admin class - PLAYER
class PlayerModelAdmin(admin.ModelAdmin):
     list_display = ('number', 'name', 'HC','total',)
     ordering = ('-total', 'number',)

# Register admin class
admin.site.register(PlayerModel, PlayerModelAdmin)

# Define new admin class - LEADERBOARD SCORING ENTRY
class EventEntryModelAdmin(admin.ModelAdmin):
     list_display = ('number', 'event', 'winner', 'points',)
     ordering = ('number',)

# Register admin class
admin.site.register(EventEntryModel, EventEntryModelAdmin)

# Define new admin class - LEADERBOARD DISPLAY
class LeaderBoardModelAdmin(admin.ModelAdmin):
     list_display = ('player', 'total_points',)
     ordering = ('total_points',)

# Register admin class
admin.site.register(LeaderBoardModel, LeaderBoardModelAdmin)

# Define new admin class - RD 1 HOLE
class Rd1HoleModelAdmin(admin.ModelAdmin):
     list_display = ('number', 'par', 'index', 'meters', 'CTP', 'LD', 'tussle',)
     ordering = ('number',)

# Register admin class
admin.site.register(Rd1HoleModel, Rd1HoleModelAdmin)


# Define new admin class - RD 1 SLOT
class Rd1SlotModelAdmin(admin.ModelAdmin):
     list_display = ('player_slot', 'player_name', 'player_holesplayed', 'player_score', 'player_stbl', 'player_rankscore', 'tussle_score',)
     ordering = ('player_slot',)

# Register admin class
admin.site.register(Rd1SlotModel, Rd1SlotModelAdmin)


# Define new admin class - RD 1 SCORE
class Rd1ScoreModelAdmin(admin.ModelAdmin):
     list_display = ('hole', 'slot1_score', 'slot2_score', 'slot3_score', 'ctp', 'ld',)
     ordering = ('hole',)

# Register admin class
admin.site.register(Rd1ScoreModel, Rd1ScoreModelAdmin)

# Define new admin class - RD 1 STABLEFORD
class Rd1StablefordModelAdmin(admin.ModelAdmin):
     list_display = ('hole', 'slot1_stbl', 'slot2_stbl', 'slot3_stbl', 'slot4_stbl', 'slot5_stbl', 'slot6_stbl', 'slot7_stbl', 'slot8_stbl', 'slot9_stbl', 'slot10_stbl', 'slot11_stbl', 'slot12_stbl',)
     ordering = ('hole',)

# Register admin class
admin.site.register(Rd1StablefordModel, Rd1StablefordModelAdmin)

# Define new admin class - RD 2 HOLE
class Rd2HoleModelAdmin(admin.ModelAdmin):
     list_display = ('number', 'par', 'index', 'meters', 'CTP', 'LD', 'tussle',)
     ordering = ('number',)

# Register admin class
admin.site.register(Rd2HoleModel, Rd2HoleModelAdmin)


# Define new admin class - RD 2 SLOT
class Rd2SlotModelAdmin(admin.ModelAdmin):
     list_display = ('player_slot', 'player_name', 'player_holesplayed', 'player_score', 'player_stbl', 'player_rankscore',)
     ordering = ('player_slot',)

# Register admin class
admin.site.register(Rd2SlotModel, Rd2SlotModelAdmin)


# Define new admin class - RD 2 SCORE
class Rd2ScoreModelAdmin(admin.ModelAdmin):
     list_display = ('hole', 'slot1_score', 'slot2_score', 'slot3_score', 'ctp', 'ld',)
     ordering = ('hole',)

# Register admin class
admin.site.register(Rd2ScoreModel, Rd2ScoreModelAdmin)

# Define new admin class - RD 2 STABLEFORD
class Rd2StablefordModelAdmin(admin.ModelAdmin):
     list_display = ('hole', 'slot1_stbl', 'slot2_stbl', 'slot3_stbl', 'slot4_stbl', 'slot5_stbl', 'slot6_stbl', 'slot7_stbl', 'slot8_stbl', 'slot9_stbl', 'slot10_stbl', 'slot11_stbl', 'slot12_stbl',)
     ordering = ('hole',)

# Register admin class
admin.site.register(Rd2StablefordModel, Rd2StablefordModelAdmin)

# Define new admin class - RD 3 HOLE
class Rd3HoleModelAdmin(admin.ModelAdmin):
     list_display = ('number', 'par', 'index', 'meters', 'CTP', 'LD', 'tussle',)
     ordering = ('number',)

# Register admin class
admin.site.register(Rd3HoleModel, Rd3HoleModelAdmin)


# Define new admin class - RD 3 SLOT
class Rd3SlotModelAdmin(admin.ModelAdmin):
     list_display = ('player_slot', 'player_name', 'player_holesplayed', 'player_score', 'player_stbl', 'player_rankscore',)
     ordering = ('player_slot',)

# Register admin class
admin.site.register(Rd3SlotModel, Rd3SlotModelAdmin)


# Define new admin class - RD 3 SCORE
class Rd3ScoreModelAdmin(admin.ModelAdmin):
     list_display = ('hole', 'slot1_score', 'slot2_score', 'slot3_score', 'ctp', 'ld',)
     ordering = ('hole',)

# Register admin class
admin.site.register(Rd3ScoreModel, Rd3ScoreModelAdmin)

# Define new admin class - RD 3 STABLEFORD
class Rd3StablefordModelAdmin(admin.ModelAdmin):
     list_display = ('hole', 'slot1_stbl', 'slot2_stbl', 'slot3_stbl', 'slot4_stbl', 'slot5_stbl', 'slot6_stbl', 'slot7_stbl', 'slot8_stbl', 'slot9_stbl', 'slot10_stbl', 'slot11_stbl', 'slot12_stbl',)
     ordering = ('hole',)

# Register admin class
admin.site.register(Rd3StablefordModel, Rd3StablefordModelAdmin)

#Define new admin class - TIP ENTRY
class SportsTippingModelAdmin(admin.ModelAdmin):
     list_display = ('name', 'time', 'password', 'game1', 'game2', 'game3', 'game4', 'game5', 'game6', 'game7', 'game8', 'game9', 'game10',)
     ordering = ('time',)
     
#Register admin class
admin.site.register(SportsTippingModel, SportsTippingModelAdmin)

#Define new admin class - TIP RESULTS
class SportsTippingResultsModelAdmin(admin.ModelAdmin):
     list_display = ('name', 'result1', 'result2', 'result3', 'result4', 'result5', 'result6', 'result7', 'result8', 'result9', 'result10',)
     
#Register admin class
admin.site.register(SportsTippingResultsModel, SportsTippingResultsModelAdmin)

#Define new admin class - TIP SCORE RECORDING
class SportsTippingScoreModelAdmin(admin.ModelAdmin):
     list_display = ('name', 'time', 'total',)
     
#Register admin class
admin.site.register(SportsTippingScoreModel, SportsTippingScoreModelAdmin)

#Define new admin class - FRIDAY SOCIAL
class FridaySocialModelAdmin(admin.ModelAdmin):
     list_display = ('name', 'password', 'best', 'honorable',)
     
#Register admin class
admin.site.register(FridaySocialModel, FridaySocialModelAdmin)

#Define new admin class - SATURDAY SOCIAL
class SaturdaySocialModelAdmin(admin.ModelAdmin):
     list_display = ('name', 'password', 'best', 'honorable',)
     
#Register admin class
admin.site.register(SaturdaySocialModel, SaturdaySocialModelAdmin)

#Define new admin class - TOUR EVENTS
class TourAgendaModelAdmin(admin.ModelAdmin):
     list_display = ('day', 'time', 'event', 'number',)
     ordering = ('number',)
     
#Register admin class
admin.site.register(TourAgendaModel, TourAgendaModelAdmin)

#Define new admin class - TOP GOLF
class TopGolfModelAdmin(admin.ModelAdmin):
     list_display = ('reference', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth',)
     
#Register admin class
admin.site.register(TopGolfModel, TopGolfModelAdmin)


#Define new admin class - RACING
class RacingModelAdmin(admin.ModelAdmin):
     list_display = ('reference', 'first', 'second', 'third', 'fourth', 'fifth', 'sixth',)
     
#Register admin class
admin.site.register(RacingModel, RacingModelAdmin)

