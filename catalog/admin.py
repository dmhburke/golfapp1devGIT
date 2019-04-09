from django.contrib import admin

# Register your models here.

from catalog.models import PlayerModel, Rd1HoleModel, Rd1SlotModel, Rd1ScoreModel, Rd1StablefordModel, SportsTippingModel, EventEntryModel, LeaderBoardModel

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

# Define new admin class - HOLE
class Rd1HoleModelAdmin(admin.ModelAdmin):
     list_display = ('number', 'par', 'index', 'meters', 'CTP', 'LD', 'tussle',)
     ordering = ('number',)

# Register admin class
admin.site.register(Rd1HoleModel, Rd1HoleModelAdmin)


# Define new admin class - SLOT
class Rd1SlotModelAdmin(admin.ModelAdmin):
     list_display = ('player_slot', 'player_name', 'player_holesplayed', 'player_score', 'player_stbl', 'player_rankscore',)
     ordering = ('player_slot',)

# Register admin class
admin.site.register(Rd1SlotModel, Rd1SlotModelAdmin)


# Define new admin class - SCORE
class Rd1ScoreModelAdmin(admin.ModelAdmin):
     list_display = ('hole', 'slot1_score', 'slot2_score', 'slot3_score', 'ctp', 'ld',)
     ordering = ('hole',)

# Register admin class
admin.site.register(Rd1ScoreModel, Rd1ScoreModelAdmin)

# Define new admin class - STABLEFORD
class Rd1StablefordModelAdmin(admin.ModelAdmin):
     list_display = ('hole', 'slot1_stbl', 'slot2_stbl', 'slot3_stbl',)
     ordering = ('hole',)

# Register admin class
admin.site.register(Rd1StablefordModel, Rd1StablefordModelAdmin)


# Define new admin class - TIPPING
class SportsTippingModelAdmin(admin.ModelAdmin):
     list_display = ('name', 'tip1',)

# Register admin class
admin.site.register(SportsTippingModel, SportsTippingModelAdmin)

