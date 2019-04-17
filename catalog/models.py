from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from catalog.choices import *
from django.db.models import Sum, Count
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class PlayerModel(models.Model):
    number = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=30)
    HC = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='playerimages', blank=True, null=True)
    jacket = models.CharField(max_length=10,choices=YES_NO,blank=True, null=True)
    tournum = models.IntegerField(blank=True, null=True)
    nickname = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, default=0, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-total']

class EventEntryModel(models.Model):
    number = models.IntegerField(blank=True, null=True)
    event = models.CharField(max_length=30)
    points = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    winner = models.ForeignKey('PlayerModel',on_delete = models.CASCADE, blank=True, null=True)

@receiver(post_save, sender=EventEntryModel)
def leaderboard_update(sender, **kwargs):

    try:
        player1 = PlayerModel.objects.get(number=1).name
    except:
        player1 = None
    try:
        player2 = PlayerModel.objects.get(number=2).name
    except:
        player2 = None
    try:
        player3 = PlayerModel.objects.get(number=3).name
    except:
        player3 = None
    try:
        player4 = PlayerModel.objects.get(number=4).name
    except:
        player4 = None
    try:
        player5 = PlayerModel.objects.get(number=5).name
    except:
        player5 = None
    try:
        player6 = PlayerModel.objects.get(number=6).name
    except:
        player6 = None
    try:
        player7 = PlayerModel.objects.get(number=7).name
    except:
        player7 = None
    try:
        player8 = PlayerModel.objects.get(number=8).name
    except:
        player8 = None
    try:
        player9 = PlayerModel.objects.get(number=9).name
    except:
        player9 = None
    try:
        player10 = PlayerModel.objects.get(number=10).name
    except:
        player10 = None
    try:
        player11 = PlayerModel.objects.get(number=11).name
    except:
        player11 = None
    try:
        player12 = PlayerModel.objects.get(number=12).name
    except:
        player12 = None

    if player1 is not None:
        player1points = list(EventEntryModel.objects.filter(winner__name=player1).aggregate(Sum('points')).values())[0]
        if player1points is None:
            player1pointsAdj = 0
        else:
            player1pointsAdj = player1points
        player1total, created = PlayerModel.objects.update_or_create(
            name=player1, defaults ={'total': player1pointsAdj,})

    if player2 is not None:
        player2points = list(EventEntryModel.objects.filter(winner__name=player2).aggregate(Sum('points')).values())[0]
        if player2points is None:
            player2pointsAdj = 0
        else:
            player2pointsAdj = player2points
        player1total, created = PlayerModel.objects.update_or_create(
            name=player2, defaults ={'total': player2pointsAdj,})

    if player3 is not None:
        player3points = list(EventEntryModel.objects.filter(winner__name=player3).aggregate(Sum('points')).values())[0]
        if player3points is None:
            player3pointsAdj = 0
        else:
            player3pointsAdj = player3points
        player3total, created = PlayerModel.objects.update_or_create(
            name=player3, defaults ={'total': player3pointsAdj,})

    if player4 is not None:
        player4points = list(EventEntryModel.objects.filter(winner__name=player4).aggregate(Sum('points')).values())[0]
        if player4points is None:
            player4pointsAdj = 0
        else:
            player4pointsAdj = player4points
        player4total, created = PlayerModel.objects.update_or_create(
            name=player4, defaults ={'total': player4pointsAdj,})

    if player5 is not None:
        player5points = list(EventEntryModel.objects.filter(winner__name=player5).aggregate(Sum('points')).values())[0]
        if player5points is None:
            player5pointsAdj = 0
        else:
            player5pointsAdj = player5points
        player5total, created = PlayerModel.objects.update_or_create(
            name=player5, defaults ={'total': player5pointsAdj,})

    if player6 is not None:
        player6points = list(EventEntryModel.objects.filter(winner__name=player6).aggregate(Sum('points')).values())[0]
        if player6points is None:
            player6pointsAdj = 0
        else:
            player6pointsAdj = player6points
        player6total, created = PlayerModel.objects.update_or_create(
            name=player6, defaults ={'total': player6pointsAdj,})

    if player7 is not None:
        player7points = list(EventEntryModel.objects.filter(winner__name=player7).aggregate(Sum('points')).values())[0]
        if player7points is None:
            player7pointsAdj = 0
        else:
            player7pointsAdj = player7points
        player7total, created = PlayerModel.objects.update_or_create(
            name=player7, defaults ={'total': player7pointsAdj,})

    if player8 is not None:
        player8points = list(EventEntryModel.objects.filter(winner__name=player8).aggregate(Sum('points')).values())[0]
        if player8points is None:
            player8pointsAdj = 0
        else:
            player8pointsAdj = player8points
        player8total, created = PlayerModel.objects.update_or_create(
            name=player8, defaults ={'total': player8pointsAdj,})

    if player9 is not None:
        player9points = list(EventEntryModel.objects.filter(winner__name=player9).aggregate(Sum('points')).values())[0]
        if player9points is None:
            player9pointsAdj = 0
        else:
            player9pointsAdj = player9points
        player9total, created = PlayerModel.objects.update_or_create(
            name=player9, defaults ={'total': player9pointsAdj,})

    if player10 is not None:
        player10points = list(EventEntryModel.objects.filter(winner__name=player10).aggregate(Sum('points')).values())[0]
        if player10points is None:
            player10pointsAdj = 0
        else:
            player10pointsAdj = player10points
        player10total, created = PlayerModel.objects.update_or_create(
            name=player10, defaults ={'total': player10pointsAdj,})

    if player11 is not None:
        player11points = list(EventEntryModel.objects.filter(winner__name=player11).aggregate(Sum('points')).values())[0]
        if player11points is None:
            player11pointsAdj = 0
        else:
            player11pointsAdj = player11points
        player11total, created = PlayerModel.objects.update_or_create(
            name=player11, defaults ={'total': player11pointsAdj,})

    if player12 is not None:
        player12points = list(EventEntryModel.objects.filter(winner__name=player12).aggregate(Sum('points')).values())[0]
        if player12points is None:
            player12pointsAdj = 0
        else:
            player12pointsAdj = player12points
        player12total, created = PlayerModel.objects.update_or_create(
            name=player12, defaults ={'total': player12pointsAdj,})

class LeaderBoardModel(models.Model):
    player = models.ForeignKey('PlayerModel', on_delete = models.CASCADE, blank=True, null=True)
    total_points = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    class Meta:
        ordering = ['total_points', 'player__HC']

## -- START ROUND 1 -- ##
class Rd1HoleModel(models.Model):
    number = models.IntegerField(primary_key=True)
    par = models.IntegerField(blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    meters = models.IntegerField(blank=True, null=True)
    CTP = models.IntegerField(validators=[MaxValueValidator(4)], blank=True, null=True)
    LD = models.IntegerField(validators=[MaxValueValidator(2)], blank=True, null=True)
    tussle = models.CharField(max_length=10,choices=YES_NO,blank=True, null=True)

    #Enables individual model records to be displayed
    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('rd1holedetail', args=[str(self.pk)])

    class Meta:
        ordering = ['number']

    def __str__(self):
        return '%d' % self.number

class Rd1SlotModel(models.Model):
    player_slot = models.IntegerField(unique=True, validators=[MaxValueValidator(12),MinValueValidator(1)])
    player_name = models.ForeignKey('PlayerModel',on_delete = models.CASCADE, blank=True, null=True)
    player_holesplayed = models.IntegerField(blank=True, null=True)
    player_score = models.IntegerField(blank=True, null=True)
    player_stbl = models.IntegerField(blank=True, null=True)
    player_rankscore = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    tussle_score = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['-player_rankscore', '-tussle_score', 'player_name__HC']


class Rd1ScoreModel(models.Model):
    hole = models.ForeignKey('Rd1HoleModel', on_delete = models.CASCADE)
    ctp = models.ForeignKey('PlayerModel', related_name="RD1ctp", on_delete = models.CASCADE, blank=True, null=True)
    ld = models.ForeignKey('PlayerModel', related_name="RD1ld", on_delete = models.CASCADE, blank=True, null=True)
    slot1_score = models.IntegerField(blank=True, null=True)
    slot2_score = models.IntegerField(blank=True, null=True)
    slot3_score = models.IntegerField(blank=True, null=True)
    slot4_score = models.IntegerField(blank=True, null=True)
    slot5_score = models.IntegerField(blank=True, null=True)
    slot6_score = models.IntegerField(blank=True, null=True)
    slot7_score = models.IntegerField(blank=True, null=True)
    slot8_score = models.IntegerField(blank=True, null=True)
    slot9_score = models.IntegerField(blank=True, null=True)
    slot10_score = models.IntegerField(blank=True, null=True)
    slot11_score = models.IntegerField(blank=True, null=True)
    slot12_score = models.IntegerField(blank=True, null=True)
    


class Rd1StablefordModel(models.Model):
    hole = models.ForeignKey('Rd1HoleModel', on_delete = models.CASCADE)
    slot1_stbl = models.IntegerField(blank=True, null=True)
    slot2_stbl = models.IntegerField(blank=True, null=True)
    slot3_stbl = models.IntegerField(blank=True, null=True)
    slot4_stbl = models.IntegerField(blank=True, null=True)
    slot5_stbl = models.IntegerField(blank=True, null=True)
    slot6_stbl = models.IntegerField(blank=True, null=True)
    slot7_stbl = models.IntegerField(blank=True, null=True)
    slot8_stbl = models.IntegerField(blank=True, null=True)
    slot9_stbl = models.IntegerField(blank=True, null=True)
    slot10_stbl = models.IntegerField(blank=True, null=True)
    slot11_stbl = models.IntegerField(blank=True, null=True)
    slot12_stbl = models.IntegerField(blank=True, null=True)

@receiver(pre_save, sender=Rd1ScoreModel)
def my_callback(sender, instance, **kwargs):

    index = instance.hole.index
    par = instance.hole.par
    hole = instance.hole
    stblford_two = 2
        
    def HC_setup():
        try:
            player1HC = Rd1SlotModel.objects.get(player_slot = 1).player_name.HC
        except:
            player1HC = 1
        try:
            player2HC = Rd1SlotModel.objects.get(player_slot = 2).player_name.HC
        except:
            player2HC = 1
        try:
            player3HC = Rd1SlotModel.objects.get(player_slot = 3).player_name.HC
        except:
            player3HC = 1
        try:
            player4HC = Rd1SlotModel.objects.get(player_slot = 4).player_name.HC
        except:
            player4HC = 1
        try:
            player5HC = Rd1SlotModel.objects.get(player_slot = 5).player_name.HC
        except:
            player5HC = 1
        try:
            player6HC = Rd1SlotModel.objects.get(player_slot = 6).player_name.HC
        except:
            player6HC = 1
        try:
            player7HC = Rd1SlotModel.objects.get(player_slot = 7).player_name.HC
        except:
            player7HC = 1
        try:
            player8HC = Rd1SlotModel.objects.get(player_slot = 8).player_name.HC
        except:
            player8HC = 1
        try:
            player9HC = Rd1SlotModel.objects.get(player_slot = 9).player_name.HC
        except:
            player9HC = 1
        try:
            player10HC = Rd1SlotModel.objects.get(player_slot = 10).player_name.HC
        except:
            player10HC = 1
        try:
            player11HC = Rd1SlotModel.objects.get(player_slot = 11).player_name.HC
        except:
            player11HC = 1
        try:
            player12HC = Rd1SlotModel.objects.get(player_slot = 12).player_name.HC
        except:
            player12HC = 1

        return (player1HC, player2HC, player3HC, player4HC, player5HC, player6HC, player7HC, player8HC, player9HC, player10HC, player11HC, player12HC)

    player1HC, player2HC, player3HC, player4HC, player5HC, player6HC, player7HC, player8HC, player9HC, player10HC, player11HC, player12HC = HC_setup()

    def stableford_conversion(par, index, HC, score):
        
        if HC >= index + 18:
            stblford_add = 2
        elif HC >= index:
            stblford_add = 1
        else:
            stblford_add = 0

        if score is None:
            score = 20        

        score_diff = par - score
        stableford_conversion = max(stblford_add + stblford_two + score_diff,0)

        return stableford_conversion

    convertedscore1 = stableford_conversion(par, index, player1HC, instance.slot1_score)
    convertedscore2 = stableford_conversion(par, index, player2HC, instance.slot2_score)
    convertedscore3 = stableford_conversion(par, index, player3HC, instance.slot3_score)
    convertedscore4 = stableford_conversion(par, index, player4HC, instance.slot4_score)
    convertedscore5 = stableford_conversion(par, index, player5HC, instance.slot5_score)
    convertedscore6 = stableford_conversion(par, index, player6HC, instance.slot6_score)
    convertedscore7 = stableford_conversion(par, index, player7HC, instance.slot7_score)
    convertedscore8 = stableford_conversion(par, index, player8HC, instance.slot8_score)
    convertedscore9 = stableford_conversion(par, index, player9HC, instance.slot9_score)
    convertedscore10 = stableford_conversion(par, index, player10HC, instance.slot10_score)
    convertedscore11 = stableford_conversion(par, index, player11HC, instance.slot11_score)
    convertedscore12 = stableford_conversion(par, index, player12HC, instance.slot12_score)
        
    stableford_scores, created = Rd1StablefordModel.objects.update_or_create(
        hole=hole,
        defaults ={
            'slot1_stbl': convertedscore1,
            'slot2_stbl': convertedscore2,
            'slot3_stbl': convertedscore3,
            'slot4_stbl': convertedscore4,
            'slot5_stbl': convertedscore5,
            'slot6_stbl': convertedscore6,
            'slot7_stbl': convertedscore7,
            'slot8_stbl': convertedscore8,
            'slot9_stbl': convertedscore9,
            'slot10_stbl': convertedscore10,
            'slot11_stbl': convertedscore11,
            'slot12_stbl': convertedscore12,
            },
        )

    player1_stablefordtotal = list(Rd1StablefordModel.objects.aggregate(Sum('slot1_stbl')).values())[0]
    player2_stablefordtotal = list(Rd1StablefordModel.objects.aggregate(Sum('slot2_stbl')).values())[0]
    player3_stablefordtotal = list(Rd1StablefordModel.objects.aggregate(Sum('slot3_stbl')).values())[0]    
    player4_stablefordtotal = list(Rd1StablefordModel.objects.aggregate(Sum('slot4_stbl')).values())[0]    
    player5_stablefordtotal = list(Rd1StablefordModel.objects.aggregate(Sum('slot5_stbl')).values())[0]    
    player6_stablefordtotal = list(Rd1StablefordModel.objects.aggregate(Sum('slot6_stbl')).values())[0]    
    player7_stablefordtotal = list(Rd1StablefordModel.objects.aggregate(Sum('slot7_stbl')).values())[0]    
    player8_stablefordtotal = list(Rd1StablefordModel.objects.aggregate(Sum('slot8_stbl')).values())[0]    
    player9_stablefordtotal = list(Rd1StablefordModel.objects.aggregate(Sum('slot9_stbl')).values())[0]    
    player10_stablefordtotal = list(Rd1StablefordModel.objects.aggregate(Sum('slot10_stbl')).values())[0]    
    player11_stablefordtotal = list(Rd1StablefordModel.objects.aggregate(Sum('slot11_stbl')).values())[0]    
    player12_stablefordtotal = list(Rd1StablefordModel.objects.aggregate(Sum('slot12_stbl')).values())[0]

    player1total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=1, defaults ={'player_stbl': player1_stablefordtotal,},)

    player2total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=2, defaults ={'player_stbl': player2_stablefordtotal,},)

    player3total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=3, defaults ={'player_stbl': player3_stablefordtotal,},)

    player4total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=4,
        defaults ={'player_stbl': player4_stablefordtotal,},)

    player5total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=5,
        defaults ={'player_stbl': player5_stablefordtotal,},)

    player6total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=6,
        defaults ={'player_stbl': player6_stablefordtotal,},)

    player7total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=7,
        defaults ={'player_stbl': player7_stablefordtotal,},)

    player8total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=8, defaults ={'player_stbl': player8_stablefordtotal,},)

    player9total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=9,
        defaults ={'player_stbl': player9_stablefordtotal,},)

    player10total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=10,
        defaults ={'player_stbl': player10_stablefordtotal,},)

    player11total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=11,
        defaults ={'player_stbl': player11_stablefordtotal,},)

    player12total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=12,
        defaults ={'player_stbl': player12_stablefordtotal,},)

@receiver(post_save, sender=Rd1ScoreModel)
def my_callback_two(sender, instance, **kwargs):

    player1_holesplayed = Rd1ScoreModel.objects.filter(slot1_score__gt=0).count()
    player2_holesplayed = Rd1ScoreModel.objects.filter(slot2_score__gt=0).count()
    player3_holesplayed = Rd1ScoreModel.objects.filter(slot3_score__gt=0).count()
    player4_holesplayed = Rd1ScoreModel.objects.filter(slot4_score__gt=0).count()
    player5_holesplayed = Rd1ScoreModel.objects.filter(slot5_score__gt=0).count()
    player6_holesplayed = Rd1ScoreModel.objects.filter(slot6_score__gt=0).count()
    player7_holesplayed = Rd1ScoreModel.objects.filter(slot7_score__gt=0).count()
    player8_holesplayed = Rd1ScoreModel.objects.filter(slot8_score__gt=0).count()
    player9_holesplayed = Rd1ScoreModel.objects.filter(slot9_score__gt=0).count()
    player10_holesplayed = Rd1ScoreModel.objects.filter(slot10_score__gt=0).count()
    player11_holesplayed = Rd1ScoreModel.objects.filter(slot11_score__gt=0).count()
    player12_holesplayed = Rd1ScoreModel.objects.filter(slot12_score__gt=0).count()

    player1_stroketotal = list(Rd1ScoreModel.objects.aggregate(Sum('slot1_score')).values())[0]
    player2_stroketotal = list(Rd1ScoreModel.objects.aggregate(Sum('slot2_score')).values())[0]
    player3_stroketotal = list(Rd1ScoreModel.objects.aggregate(Sum('slot3_score')).values())[0]
    player4_stroketotal = list(Rd1ScoreModel.objects.aggregate(Sum('slot4_score')).values())[0]
    player5_stroketotal = list(Rd1ScoreModel.objects.aggregate(Sum('slot5_score')).values())[0]
    player6_stroketotal = list(Rd1ScoreModel.objects.aggregate(Sum('slot6_score')).values())[0]
    player7_stroketotal = list(Rd1ScoreModel.objects.aggregate(Sum('slot7_score')).values())[0]
    player8_stroketotal = list(Rd1ScoreModel.objects.aggregate(Sum('slot8_score')).values())[0]
    player9_stroketotal = list(Rd1ScoreModel.objects.aggregate(Sum('slot9_score')).values())[0]
    player10_stroketotal = list(Rd1ScoreModel.objects.aggregate(Sum('slot10_score')).values())[0]
    player11_stroketotal = list(Rd1ScoreModel.objects.aggregate(Sum('slot11_score')).values())[0]
    player12_stroketotal = list(Rd1ScoreModel.objects.aggregate(Sum('slot12_score')).values())[0]
    
    tussle_hole = Rd1HoleModel.objects.filter(tussle__isnull=False)

    tussle_sum1 = list(Rd1StablefordModel.objects.filter(hole__tussle="YES").aggregate(Sum('slot1_stbl')).values())[0]
    tussle_sum2 = list(Rd1StablefordModel.objects.filter(hole__tussle="YES").aggregate(Sum('slot2_stbl')).values())[0]
    tussle_sum3 = list(Rd1StablefordModel.objects.filter(hole__tussle="YES").aggregate(Sum('slot3_stbl')).values())[0]
    tussle_sum4 = list(Rd1StablefordModel.objects.filter(hole__tussle="YES").aggregate(Sum('slot4_stbl')).values())[0]
    tussle_sum5 = list(Rd1StablefordModel.objects.filter(hole__tussle="YES").aggregate(Sum('slot5_stbl')).values())[0]
    tussle_sum6 = list(Rd1StablefordModel.objects.filter(hole__tussle="YES").aggregate(Sum('slot6_stbl')).values())[0]
    tussle_sum7 = list(Rd1StablefordModel.objects.filter(hole__tussle="YES").aggregate(Sum('slot7_stbl')).values())[0]
    tussle_sum8 = list(Rd1StablefordModel.objects.filter(hole__tussle="YES").aggregate(Sum('slot8_stbl')).values())[0]
    tussle_sum9 = list(Rd1StablefordModel.objects.filter(hole__tussle="YES").aggregate(Sum('slot9_stbl')).values())[0]
    tussle_sum10 = list(Rd1StablefordModel.objects.filter(hole__tussle="YES").aggregate(Sum('slot10_stbl')).values())[0]
    tussle_sum11 = list(Rd1StablefordModel.objects.filter(hole__tussle="YES").aggregate(Sum('slot11_stbl')).values())[0]
    tussle_sum12 = list(Rd1StablefordModel.objects.filter(hole__tussle="YES").aggregate(Sum('slot12_stbl')).values())[0]
    
    player1total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=1,
        defaults ={'player_holesplayed': player1_holesplayed, 'player_score': player1_stroketotal, 'tussle_score': tussle_sum1,},)

    player2total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=2,
        defaults ={'player_holesplayed': player2_holesplayed, 'player_score': player2_stroketotal, 'tussle_score': tussle_sum2,},)

    player3total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=3,
        defaults ={'player_holesplayed': player3_holesplayed, 'player_score': player3_stroketotal, 'tussle_score': tussle_sum3,},)

    player4total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=4,
        defaults ={'player_holesplayed': player4_holesplayed, 'player_score': player4_stroketotal, 'tussle_score': tussle_sum4,},)

    player5total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=5,
        defaults ={'player_holesplayed': player5_holesplayed, 'player_score': player5_stroketotal, 'tussle_score': tussle_sum5,},)

    player6total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=6,
        defaults ={'player_holesplayed': player6_holesplayed, 'player_score': player6_stroketotal, 'tussle_score': tussle_sum6,},)

    player7total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=7,
        defaults ={'player_holesplayed': player7_holesplayed, 'player_score': player7_stroketotal, 'tussle_score': tussle_sum7,},)

    player8total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=8,
        defaults ={'player_holesplayed': player8_holesplayed, 'player_score': player8_stroketotal, 'tussle_score': tussle_sum8,},)

    player9total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=9,
        defaults ={'player_holesplayed': player9_holesplayed, 'player_score': player9_stroketotal, 'tussle_score': tussle_sum9,},)

    player10total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=10,
        defaults ={'player_holesplayed': player10_holesplayed, 'player_score': player10_stroketotal, 'tussle_score': tussle_sum10,},)

    player11total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=11,
        defaults ={'player_holesplayed': player11_holesplayed, 'player_score': player11_stroketotal, 'tussle_score': tussle_sum11,},)

    player12total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=12,
        defaults ={'player_holesplayed': player12_holesplayed, 'player_score': player12_stroketotal, 'tussle_score': tussle_sum12,},)
    
#RANKINGSCORES CALCS
    
    player1_stablefordtotal1 = list(Rd1StablefordModel.objects.aggregate(Sum('slot1_stbl')).values())[0]
    player2_stablefordtotal1 = list(Rd1StablefordModel.objects.aggregate(Sum('slot2_stbl')).values())[0]
    player3_stablefordtotal1 = list(Rd1StablefordModel.objects.aggregate(Sum('slot3_stbl')).values())[0]    
    player4_stablefordtotal1 = list(Rd1StablefordModel.objects.aggregate(Sum('slot4_stbl')).values())[0]    
    player5_stablefordtotal1 = list(Rd1StablefordModel.objects.aggregate(Sum('slot5_stbl')).values())[0]    
    player6_stablefordtotal1 = list(Rd1StablefordModel.objects.aggregate(Sum('slot6_stbl')).values())[0]    
    player7_stablefordtotal1 = list(Rd1StablefordModel.objects.aggregate(Sum('slot7_stbl')).values())[0]    
    player8_stablefordtotal1 = list(Rd1StablefordModel.objects.aggregate(Sum('slot8_stbl')).values())[0]    
    player9_stablefordtotal1 = list(Rd1StablefordModel.objects.aggregate(Sum('slot9_stbl')).values())[0]    
    player10_stablefordtotal1 = list(Rd1StablefordModel.objects.aggregate(Sum('slot10_stbl')).values())[0]    
    player11_stablefordtotal1 = list(Rd1StablefordModel.objects.aggregate(Sum('slot11_stbl')).values())[0]    
    player12_stablefordtotal1 = list(Rd1StablefordModel.objects.aggregate(Sum('slot12_stbl')).values())[0]

    try:
        player1_rankscore = player1_stablefordtotal1/player1_holesplayed
    except:
        player1_rankscore = 0
    try:
        player2_rankscore = player2_stablefordtotal1/player2_holesplayed
    except:
        player2_rankscore = 0
    try:
        player3_rankscore = player3_stablefordtotal1/player3_holesplayed
    except:
        player3_rankscore = 0
    try:
        player4_rankscore = player4_stablefordtotal1/player4_holesplayed
    except:
        player4_rankscore = 0
    try:
        player5_rankscore = player5_stablefordtotal1/player5_holesplayed
    except:
        player5_rankscore = 0
    try:
        player6_rankscore = player6_stablefordtotal1/player6_holesplayed
    except:
        player6_rankscore = 0
    try:
        player7_rankscore = player7_stablefordtotal1/player7_holesplayed
    except:
        player7_rankscore = 0
    try:
        player8_rankscore = player8_stablefordtotal1/player8_holesplayed
    except:
        player8_rankscore = 0
    try:
        player9_rankscore = player9_stablefordtotal1/player9_holesplayed
    except:
        player9_rankscore = 0
    try:
        player10_rankscore = player10_stablefordtotal1/player10_holesplayed
    except:
        player10_rankscore = 0
    try:
        player11_rankscore = player11_stablefordtotal1/player11_holesplayed
    except:
        player11_rankscore = 0
    try:
        player12_rankscore = player12_stablefordtotal1/player12_holesplayed
    except:
        player12_rankscore = 0

    player1total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=1, defaults ={'player_rankscore': player1_rankscore,},)
    player2total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=2, defaults ={'player_rankscore': player2_rankscore,},)
    player3total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=3, defaults ={'player_rankscore': player3_rankscore,},)
    player4total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=4, defaults ={'player_rankscore': player4_rankscore,},)
    player5total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=5, defaults ={'player_rankscore': player5_rankscore,},)
    player6total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=6, defaults ={'player_rankscore': player6_rankscore,},)
    player7total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=7, defaults ={'player_rankscore': player7_rankscore,},)
    player8total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=8, defaults ={'player_rankscore': player8_rankscore,},)
    player9total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=9, defaults ={'player_rankscore': player9_rankscore,},)
    player10total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=10, defaults ={'player_rankscore': player10_rankscore,},)
    player11total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=11, defaults ={'player_rankscore': player11_rankscore,},)
    player12total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=12, defaults ={'player_rankscore': player12_rankscore,},)

## -- END ROUND 1 -- ##

## --START ROUND 2 --##
class Rd2HoleModel(models.Model):
    number = models.IntegerField(primary_key=True)
    par = models.IntegerField(blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    meters = models.IntegerField(blank=True, null=True)
    CTP = models.IntegerField(validators=[MaxValueValidator(4)], blank=True, null=True)
    LD = models.IntegerField(validators=[MaxValueValidator(2)], blank=True, null=True)
    tussle = models.CharField(max_length=10,choices=YES_NO,blank=True, null=True)

    #Enables individual model records to be displayed
    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('rd2holedetail', args=[str(self.pk)])

    class Meta:
        ordering = ['number']

    def __str__(self):
        return '%d' % self.number

class Rd2SlotModel(models.Model):
    player_slot = models.IntegerField(unique=True, validators=[MaxValueValidator(12),MinValueValidator(1)])
    player_name = models.ForeignKey('PlayerModel',on_delete = models.CASCADE, blank=True, null=True)
    player_holesplayed = models.IntegerField(blank=True, null=True)
    player_score = models.IntegerField(blank=True, null=True)
    player_stbl = models.IntegerField(blank=True, null=True)
    player_rankscore = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    tussle_score = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['-player_rankscore', '-tussle_score', 'player_name__HC']


class Rd2ScoreModel(models.Model):
    hole = models.ForeignKey('Rd2HoleModel', on_delete = models.CASCADE)
    ctp = models.ForeignKey('PlayerModel', related_name="RD2ctp", on_delete = models.CASCADE, blank=True, null=True)
    ld = models.ForeignKey('PlayerModel', related_name="RD2ld", on_delete = models.CASCADE, blank=True, null=True)
    slot1_score = models.IntegerField(blank=True, null=True)
    slot2_score = models.IntegerField(blank=True, null=True)
    slot3_score = models.IntegerField(blank=True, null=True)
    slot4_score = models.IntegerField(blank=True, null=True)
    slot5_score = models.IntegerField(blank=True, null=True)
    slot6_score = models.IntegerField(blank=True, null=True)
    slot7_score = models.IntegerField(blank=True, null=True)
    slot8_score = models.IntegerField(blank=True, null=True)
    slot9_score = models.IntegerField(blank=True, null=True)
    slot10_score = models.IntegerField(blank=True, null=True)
    slot11_score = models.IntegerField(blank=True, null=True)
    slot12_score = models.IntegerField(blank=True, null=True)
    


class Rd2StablefordModel(models.Model):
    hole = models.ForeignKey('Rd2HoleModel', on_delete = models.CASCADE)
    slot1_stbl = models.IntegerField(blank=True, null=True)
    slot2_stbl = models.IntegerField(blank=True, null=True)
    slot3_stbl = models.IntegerField(blank=True, null=True)
    slot4_stbl = models.IntegerField(blank=True, null=True)
    slot5_stbl = models.IntegerField(blank=True, null=True)
    slot6_stbl = models.IntegerField(blank=True, null=True)
    slot7_stbl = models.IntegerField(blank=True, null=True)
    slot8_stbl = models.IntegerField(blank=True, null=True)
    slot9_stbl = models.IntegerField(blank=True, null=True)
    slot10_stbl = models.IntegerField(blank=True, null=True)
    slot11_stbl = models.IntegerField(blank=True, null=True)
    slot12_stbl = models.IntegerField(blank=True, null=True)

@receiver(pre_save, sender=Rd2ScoreModel)
def round2_callback(sender, instance, **kwargs):

    index = instance.hole.index
    par = instance.hole.par
    hole = instance.hole
    stblford_two = 2
        
    def HC_setup():
        try:
            player1HC = Rd2SlotModel.objects.get(player_slot = 1).player_name.HC
        except:
            player1HC = 1
        try:
            player2HC = Rd2SlotModel.objects.get(player_slot = 2).player_name.HC
        except:
            player2HC = 1
        try:
            player3HC = Rd2SlotModel.objects.get(player_slot = 3).player_name.HC
        except:
            player3HC = 1
        try:
            player4HC = Rd2SlotModel.objects.get(player_slot = 4).player_name.HC
        except:
            player4HC = 1
        try:
            player5HC = Rd2SlotModel.objects.get(player_slot = 5).player_name.HC
        except:
            player5HC = 1
        try:
            player6HC = Rd2SlotModel.objects.get(player_slot = 6).player_name.HC
        except:
            player6HC = 1
        try:
            player7HC = Rd2SlotModel.objects.get(player_slot = 7).player_name.HC
        except:
            player7HC = 1
        try:
            player8HC = Rd2SlotModel.objects.get(player_slot = 8).player_name.HC
        except:
            player8HC = 1
        try:
            player9HC = Rd2SlotModel.objects.get(player_slot = 9).player_name.HC
        except:
            player9HC = 1
        try:
            player10HC = Rd2SlotModel.objects.get(player_slot = 10).player_name.HC
        except:
            player10HC = 1
        try:
            player11HC = Rd2SlotModel.objects.get(player_slot = 11).player_name.HC
        except:
            player11HC = 1
        try:
            player12HC = Rd2SlotModel.objects.get(player_slot = 12).player_name.HC
        except:
            player12HC = 1

        return (player1HC, player2HC, player3HC, player4HC, player5HC, player6HC, player7HC, player8HC, player9HC, player10HC, player11HC, player12HC)

    player1HC, player2HC, player3HC, player4HC, player5HC, player6HC, player7HC, player8HC, player9HC, player10HC, player11HC, player12HC = HC_setup()

    def stableford_conversion(par, index, HC, score):
        
        if HC >= index + 18:
            stblford_add = 2
        elif HC >= index:
            stblford_add = 1
        else:
            stblford_add = 0

        if score is None:
            score = 20        

        score_diff = par - score
        stableford_conversion = max(stblford_add + stblford_two + score_diff,0)

        return stableford_conversion

    convertedscore1 = stableford_conversion(par, index, player1HC, instance.slot1_score)
    convertedscore2 = stableford_conversion(par, index, player2HC, instance.slot2_score)
    convertedscore3 = stableford_conversion(par, index, player3HC, instance.slot3_score)
    convertedscore4 = stableford_conversion(par, index, player4HC, instance.slot4_score)
    convertedscore5 = stableford_conversion(par, index, player5HC, instance.slot5_score)
    convertedscore6 = stableford_conversion(par, index, player6HC, instance.slot6_score)
    convertedscore7 = stableford_conversion(par, index, player7HC, instance.slot7_score)
    convertedscore8 = stableford_conversion(par, index, player8HC, instance.slot8_score)
    convertedscore9 = stableford_conversion(par, index, player9HC, instance.slot9_score)
    convertedscore10 = stableford_conversion(par, index, player10HC, instance.slot10_score)
    convertedscore11 = stableford_conversion(par, index, player11HC, instance.slot11_score)
    convertedscore12 = stableford_conversion(par, index, player12HC, instance.slot12_score)
        
    stableford_scores, created = Rd2StablefordModel.objects.update_or_create(
        hole=hole,
        defaults ={
            'slot1_stbl': convertedscore1,
            'slot2_stbl': convertedscore2,
            'slot3_stbl': convertedscore3,
            'slot4_stbl': convertedscore4,
            'slot5_stbl': convertedscore5,
            'slot6_stbl': convertedscore6,
            'slot7_stbl': convertedscore7,
            'slot8_stbl': convertedscore8,
            'slot9_stbl': convertedscore9,
            'slot10_stbl': convertedscore10,
            'slot11_stbl': convertedscore11,
            'slot12_stbl': convertedscore12,
            },
        )

    player1_stablefordtotal = list(Rd2StablefordModel.objects.aggregate(Sum('slot1_stbl')).values())[0]
    player2_stablefordtotal = list(Rd2StablefordModel.objects.aggregate(Sum('slot2_stbl')).values())[0]
    player3_stablefordtotal = list(Rd2StablefordModel.objects.aggregate(Sum('slot3_stbl')).values())[0]    
    player4_stablefordtotal = list(Rd2StablefordModel.objects.aggregate(Sum('slot4_stbl')).values())[0]    
    player5_stablefordtotal = list(Rd2StablefordModel.objects.aggregate(Sum('slot5_stbl')).values())[0]    
    player6_stablefordtotal = list(Rd2StablefordModel.objects.aggregate(Sum('slot6_stbl')).values())[0]    
    player7_stablefordtotal = list(Rd2StablefordModel.objects.aggregate(Sum('slot7_stbl')).values())[0]    
    player8_stablefordtotal = list(Rd2StablefordModel.objects.aggregate(Sum('slot8_stbl')).values())[0]    
    player9_stablefordtotal = list(Rd2StablefordModel.objects.aggregate(Sum('slot9_stbl')).values())[0]    
    player10_stablefordtotal = list(Rd2StablefordModel.objects.aggregate(Sum('slot10_stbl')).values())[0]    
    player11_stablefordtotal = list(Rd2StablefordModel.objects.aggregate(Sum('slot11_stbl')).values())[0]    
    player12_stablefordtotal = list(Rd2StablefordModel.objects.aggregate(Sum('slot12_stbl')).values())[0]

    player1total, created = Rd2SlotModel.objects.update_or_create(
        player_slot=1, defaults ={'player_stbl': player1_stablefordtotal,},)

    player2total, created = Rd2SlotModel.objects.update_or_create(
        player_slot=2, defaults ={'player_stbl': player2_stablefordtotal,},)

    player3total, created = Rd2SlotModel.objects.update_or_create(
        player_slot=3, defaults ={'player_stbl': player3_stablefordtotal,},)

    player4total, created = Rd2SlotModel.objects.update_or_create(
        player_slot=4,
        defaults ={
            'player_stbl': player4_stablefordtotal,
            },
        )

    player5total, created = Rd2SlotModel.objects.update_or_create(
        player_slot=5,
        defaults ={
            'player_stbl': player5_stablefordtotal,
            },
        )

    player6total, created = Rd2SlotModel.objects.update_or_create(
        player_slot=6,
        defaults ={
            'player_stbl': player6_stablefordtotal,
            },
        )

    player7total, created = Rd2SlotModel.objects.update_or_create(
        player_slot=7,
        defaults ={
            'player_stbl': player7_stablefordtotal,
            },
        )

    player8total, created = Rd2SlotModel.objects.update_or_create(
        player_slot=8,
        defaults ={
            'player_stbl': player8_stablefordtotal,
            },
        )

    player9total, created = Rd2SlotModel.objects.update_or_create(
        player_slot=9,
        defaults ={
            'player_stbl': player9_stablefordtotal,
            },
        )

    player10total, created = Rd2SlotModel.objects.update_or_create(
        player_slot=10,
        defaults ={
            'player_stbl': player10_stablefordtotal,
            },
        )

    player11total, created = Rd2SlotModel.objects.update_or_create(
        player_slot=11,
        defaults ={
            'player_stbl': player11_stablefordtotal,
            },
        )

    player12total, created = Rd2SlotModel.objects.update_or_create(
        player_slot=12,
        defaults ={
            'player_stbl': player12_stablefordtotal,
            },
        )

@receiver(post_save, sender=Rd2ScoreModel)
def round2_callback_two(sender, instance, **kwargs):

    player1_holesplayed = Rd2ScoreModel.objects.filter(slot1_score__gt=0).count()
    player2_holesplayed = Rd2ScoreModel.objects.filter(slot2_score__gt=0).count()
    player3_holesplayed = Rd2ScoreModel.objects.filter(slot3_score__gt=0).count()
    player4_holesplayed = Rd2ScoreModel.objects.filter(slot4_score__gt=0).count()
    player5_holesplayed = Rd2ScoreModel.objects.filter(slot5_score__gt=0).count()
    player6_holesplayed = Rd2ScoreModel.objects.filter(slot6_score__gt=0).count()
    player7_holesplayed = Rd2ScoreModel.objects.filter(slot7_score__gt=0).count()
    player8_holesplayed = Rd2ScoreModel.objects.filter(slot8_score__gt=0).count()
    player9_holesplayed = Rd2ScoreModel.objects.filter(slot9_score__gt=0).count()
    player10_holesplayed = Rd2ScoreModel.objects.filter(slot10_score__gt=0).count()
    player11_holesplayed = Rd2ScoreModel.objects.filter(slot11_score__gt=0).count()
    player12_holesplayed = Rd2ScoreModel.objects.filter(slot12_score__gt=0).count()

    player1_stroketotal = list(Rd2ScoreModel.objects.aggregate(Sum('slot1_score')).values())[0]
    player2_stroketotal = list(Rd2ScoreModel.objects.aggregate(Sum('slot2_score')).values())[0]
    player3_stroketotal = list(Rd2ScoreModel.objects.aggregate(Sum('slot3_score')).values())[0]
    player4_stroketotal = list(Rd2ScoreModel.objects.aggregate(Sum('slot4_score')).values())[0]
    player5_stroketotal = list(Rd2ScoreModel.objects.aggregate(Sum('slot5_score')).values())[0]
    player6_stroketotal = list(Rd2ScoreModel.objects.aggregate(Sum('slot6_score')).values())[0]
    player7_stroketotal = list(Rd2ScoreModel.objects.aggregate(Sum('slot7_score')).values())[0]
    player8_stroketotal = list(Rd2ScoreModel.objects.aggregate(Sum('slot8_score')).values())[0]
    player9_stroketotal = list(Rd2ScoreModel.objects.aggregate(Sum('slot9_score')).values())[0]
    player10_stroketotal = list(Rd2ScoreModel.objects.aggregate(Sum('slot10_score')).values())[0]
    player11_stroketotal = list(Rd2ScoreModel.objects.aggregate(Sum('slot11_score')).values())[0]
    player12_stroketotal = list(Rd2ScoreModel.objects.aggregate(Sum('slot12_score')).values())[0]
    
    tussle_hole = Rd2HoleModel.objects.filter(tussle__isnull=False)

    tussle_sum1 = list(Rd2StablefordModel.objects.filter(hole__tussle="YES").aggregate(Sum('slot1_stbl')).values())[0]
    tussle_sum2 = list(Rd2StablefordModel.objects.filter(hole__tussle="YES").aggregate(Sum('slot2_stbl')).values())[0]
    tussle_sum3 = list(Rd2StablefordModel.objects.filter(hole__tussle="YES").aggregate(Sum('slot3_stbl')).values())[0]
    tussle_sum4 = list(Rd2StablefordModel.objects.filter(hole__tussle="YES").aggregate(Sum('slot4_stbl')).values())[0]
    tussle_sum5 = list(Rd2StablefordModel.objects.filter(hole__tussle="YES").aggregate(Sum('slot5_stbl')).values())[0]
    tussle_sum6 = list(Rd2StablefordModel.objects.filter(hole__tussle="YES").aggregate(Sum('slot6_stbl')).values())[0]
    tussle_sum7 = list(Rd2StablefordModel.objects.filter(hole__tussle="YES").aggregate(Sum('slot7_stbl')).values())[0]
    tussle_sum8 = list(Rd2StablefordModel.objects.filter(hole__tussle="YES").aggregate(Sum('slot8_stbl')).values())[0]
    tussle_sum9 = list(Rd2StablefordModel.objects.filter(hole__tussle="YES").aggregate(Sum('slot9_stbl')).values())[0]
    tussle_sum10 = list(Rd2StablefordModel.objects.filter(hole__tussle="YES").aggregate(Sum('slot10_stbl')).values())[0]
    tussle_sum11 = list(Rd2StablefordModel.objects.filter(hole__tussle="YES").aggregate(Sum('slot11_stbl')).values())[0]
    tussle_sum12 = list(Rd2StablefordModel.objects.filter(hole__tussle="YES").aggregate(Sum('slot12_stbl')).values())[0]
    
    player1total, created = Rd2SlotModel.objects.update_or_create(
        player_slot=1,
        defaults ={'player_holesplayed': player1_holesplayed, 'player_score': player1_stroketotal, 'tussle_score': tussle_sum1,},)

    player2total, created = Rd2SlotModel.objects.update_or_create(
        player_slot=2,
        defaults ={'player_holesplayed': player2_holesplayed, 'player_score': player2_stroketotal, 'tussle_score': tussle_sum2,},)

    player3total, created = Rd2SlotModel.objects.update_or_create(
        player_slot=3,
        defaults ={'player_holesplayed': player3_holesplayed, 'player_score': player3_stroketotal, 'tussle_score': tussle_sum3,},)

    player4total, created = Rd2SlotModel.objects.update_or_create(
        player_slot=4,
        defaults ={'player_holesplayed': player4_holesplayed, 'player_score': player4_stroketotal, 'tussle_score': tussle_sum4,},)

    player5total, created = Rd2SlotModel.objects.update_or_create(
        player_slot=5,
        defaults ={'player_holesplayed': player5_holesplayed, 'player_score': player5_stroketotal, 'tussle_score': tussle_sum5,},)

    player6total, created = Rd2SlotModel.objects.update_or_create(
        player_slot=6,
        defaults ={'player_holesplayed': player6_holesplayed, 'player_score': player6_stroketotal, 'tussle_score': tussle_sum6,},)

    player7total, created = Rd2SlotModel.objects.update_or_create(
        player_slot=7,
        defaults ={'player_holesplayed': player7_holesplayed, 'player_score': player7_stroketotal, 'tussle_score': tussle_sum7,},)

    player8total, created = Rd2SlotModel.objects.update_or_create(
        player_slot=8,
        defaults ={'player_holesplayed': player8_holesplayed, 'player_score': player8_stroketotal, 'tussle_score': tussle_sum8,},)

    player9total, created = Rd2SlotModel.objects.update_or_create(
        player_slot=9,
        defaults ={'player_holesplayed': player9_holesplayed, 'player_score': player9_stroketotal, 'tussle_score': tussle_sum9,},)

    player10total, created = Rd2SlotModel.objects.update_or_create(
        player_slot=10,
        defaults ={'player_holesplayed': player10_holesplayed, 'player_score': player10_stroketotal, 'tussle_score': tussle_sum10,},)

    player11total, created = Rd2SlotModel.objects.update_or_create(
        player_slot=11,
        defaults ={'player_holesplayed': player11_holesplayed, 'player_score': player11_stroketotal, 'tussle_score': tussle_sum11,},)

    player12total, created = Rd2SlotModel.objects.update_or_create(
        player_slot=12,
        defaults ={'player_holesplayed': player12_holesplayed, 'player_score': player12_stroketotal, 'tussle_score': tussle_sum12,},)


#RANKINGSCORES CALCS
    
    player1_stablefordtotal1 = list(Rd2StablefordModel.objects.aggregate(Sum('slot1_stbl')).values())[0]
    player2_stablefordtotal1 = list(Rd2StablefordModel.objects.aggregate(Sum('slot2_stbl')).values())[0]
    player3_stablefordtotal1 = list(Rd2StablefordModel.objects.aggregate(Sum('slot3_stbl')).values())[0]    
    player4_stablefordtotal1 = list(Rd2StablefordModel.objects.aggregate(Sum('slot4_stbl')).values())[0]    
    player5_stablefordtotal1 = list(Rd2StablefordModel.objects.aggregate(Sum('slot5_stbl')).values())[0]    
    player6_stablefordtotal1 = list(Rd2StablefordModel.objects.aggregate(Sum('slot6_stbl')).values())[0]    
    player7_stablefordtotal1 = list(Rd2StablefordModel.objects.aggregate(Sum('slot7_stbl')).values())[0]    
    player8_stablefordtotal1 = list(Rd2StablefordModel.objects.aggregate(Sum('slot8_stbl')).values())[0]    
    player9_stablefordtotal1 = list(Rd2StablefordModel.objects.aggregate(Sum('slot9_stbl')).values())[0]    
    player10_stablefordtotal1 = list(Rd2StablefordModel.objects.aggregate(Sum('slot10_stbl')).values())[0]    
    player11_stablefordtotal1 = list(Rd2StablefordModel.objects.aggregate(Sum('slot11_stbl')).values())[0]    
    player12_stablefordtotal1 = list(Rd2StablefordModel.objects.aggregate(Sum('slot12_stbl')).values())[0]

    try:
        player1_rankscore = player1_stablefordtotal1/player1_holesplayed
    except:
        player1_rankscore = 0
    try:
        player2_rankscore = player2_stablefordtotal1/player2_holesplayed
    except:
        player2_rankscore = 0
    try:
        player3_rankscore = player3_stablefordtotal1/player3_holesplayed
    except:
        player3_rankscore = 0
    try:
        player4_rankscore = player4_stablefordtotal1/player4_holesplayed
    except:
        player4_rankscore = 0
    try:
        player5_rankscore = player5_stablefordtotal1/player5_holesplayed
    except:
        player5_rankscore = 0
    try:
        player6_rankscore = player6_stablefordtotal1/player6_holesplayed
    except:
        player6_rankscore = 0
    try:
        player7_rankscore = player7_stablefordtotal1/player7_holesplayed
    except:
        player7_rankscore = 0
    try:
        player8_rankscore = player8_stablefordtotal1/player8_holesplayed
    except:
        player8_rankscore = 0
    try:
        player9_rankscore = player9_stablefordtotal1/player9_holesplayed
    except:
        player9_rankscore = 0
    try:
        player10_rankscore = player10_stablefordtotal1/player10_holesplayed
    except:
        player10_rankscore = 0
    try:
        player11_rankscore = player11_stablefordtotal1/player11_holesplayed
    except:
        player11_rankscore = 0
    try:
        player12_rankscore = player12_stablefordtotal1/player12_holesplayed
    except:
        player12_rankscore = 0

    player1total, created = Rd2SlotModel.objects.update_or_create(
        player_slot=1, defaults ={'player_rankscore': player1_rankscore,},)
    player2total, created = Rd2SlotModel.objects.update_or_create(
        player_slot=2, defaults ={'player_rankscore': player2_rankscore,},)
    player3total, created = Rd2SlotModel.objects.update_or_create(
        player_slot=3, defaults ={'player_rankscore': player3_rankscore,},)
    player4total, created = Rd2SlotModel.objects.update_or_create(
        player_slot=4, defaults ={'player_rankscore': player4_rankscore,},)
    player5total, created = Rd2SlotModel.objects.update_or_create(
        player_slot=5, defaults ={'player_rankscore': player5_rankscore,},)
    player6total, created = Rd2SlotModel.objects.update_or_create(
        player_slot=6, defaults ={'player_rankscore': player6_rankscore,},)
    player7total, created = Rd2SlotModel.objects.update_or_create(
        player_slot=7, defaults ={'player_rankscore': player7_rankscore,},)
    player8total, created = Rd2SlotModel.objects.update_or_create(
        player_slot=8, defaults ={'player_rankscore': player8_rankscore,},)
    player9total, created = Rd2SlotModel.objects.update_or_create(
        player_slot=9, defaults ={'player_rankscore': player9_rankscore,},)
    player10total, created = Rd2SlotModel.objects.update_or_create(
        player_slot=10, defaults ={'player_rankscore': player10_rankscore,},)
    player11total, created = Rd2SlotModel.objects.update_or_create(
        player_slot=11, defaults ={'player_rankscore': player11_rankscore,},)
    player12total, created = Rd2SlotModel.objects.update_or_create(
        player_slot=12, defaults ={'player_rankscore': player12_rankscore,},)

## -- END ROUND 2 -- ##

## -- START ROUND 3 -- ##
class Rd3HoleModel(models.Model):
    number = models.IntegerField(primary_key=True)
    par = models.IntegerField(blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    meters = models.IntegerField(blank=True, null=True)
    CTP = models.IntegerField(validators=[MaxValueValidator(4)], blank=True, null=True)
    LD = models.IntegerField(validators=[MaxValueValidator(2)], blank=True, null=True)
    tussle = models.CharField(max_length=10,choices=YES_NO,blank=True, null=True)

    #Enables individual model records to be displayed
    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('rd3holedetail', args=[str(self.pk)])

    class Meta:
        ordering = ['number']

    def __str__(self):
        return '%d' % self.number

class Rd3SlotModel(models.Model):
    player_slot = models.IntegerField(unique=True, validators=[MaxValueValidator(12),MinValueValidator(1)])
    player_name = models.ForeignKey('PlayerModel',on_delete = models.CASCADE, blank=True, null=True)
    player_holesplayed = models.IntegerField(blank=True, null=True)
    player_score = models.IntegerField(blank=True, null=True)
    player_stbl = models.IntegerField(blank=True, null=True)
    player_rankscore = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    tussle_score = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['-player_rankscore', '-tussle_score', 'player_name__HC']


class Rd3ScoreModel(models.Model):
    hole = models.ForeignKey('Rd3HoleModel', on_delete = models.CASCADE)
    ctp = models.ForeignKey('PlayerModel', related_name="RD3ctp", on_delete = models.CASCADE, blank=True, null=True)
    ld = models.ForeignKey('PlayerModel', related_name="RD3ld", on_delete = models.CASCADE, blank=True, null=True)
    slot1_score = models.IntegerField(blank=True, null=True)
    slot2_score = models.IntegerField(blank=True, null=True)
    slot3_score = models.IntegerField(blank=True, null=True)
    slot4_score = models.IntegerField(blank=True, null=True)
    slot5_score = models.IntegerField(blank=True, null=True)
    slot6_score = models.IntegerField(blank=True, null=True)
    slot7_score = models.IntegerField(blank=True, null=True)
    slot8_score = models.IntegerField(blank=True, null=True)
    slot9_score = models.IntegerField(blank=True, null=True)
    slot10_score = models.IntegerField(blank=True, null=True)
    slot11_score = models.IntegerField(blank=True, null=True)
    slot12_score = models.IntegerField(blank=True, null=True)
    


class Rd3StablefordModel(models.Model):
    hole = models.ForeignKey('Rd3HoleModel', on_delete = models.CASCADE)
    slot1_stbl = models.IntegerField(blank=True, null=True)
    slot2_stbl = models.IntegerField(blank=True, null=True)
    slot3_stbl = models.IntegerField(blank=True, null=True)
    slot4_stbl = models.IntegerField(blank=True, null=True)
    slot5_stbl = models.IntegerField(blank=True, null=True)
    slot6_stbl = models.IntegerField(blank=True, null=True)
    slot7_stbl = models.IntegerField(blank=True, null=True)
    slot8_stbl = models.IntegerField(blank=True, null=True)
    slot9_stbl = models.IntegerField(blank=True, null=True)
    slot10_stbl = models.IntegerField(blank=True, null=True)
    slot11_stbl = models.IntegerField(blank=True, null=True)
    slot12_stbl = models.IntegerField(blank=True, null=True)

@receiver(pre_save, sender=Rd3ScoreModel)
def round3_callback(sender, instance, **kwargs):

    index = instance.hole.index
    par = instance.hole.par
    hole = instance.hole
    stblford_two = 2
        
    def HC_setup():
        try:
            player1HC = Rd3SlotModel.objects.get(player_slot = 1).player_name.HC
        except:
            player1HC = 1
        try:
            player2HC = Rd3SlotModel.objects.get(player_slot = 2).player_name.HC
        except:
            player2HC = 1
        try:
            player3HC = Rd3SlotModel.objects.get(player_slot = 3).player_name.HC
        except:
            player3HC = 1
        try:
            player4HC = Rd3SlotModel.objects.get(player_slot = 4).player_name.HC
        except:
            player4HC = 1
        try:
            player5HC = Rd3SlotModel.objects.get(player_slot = 5).player_name.HC
        except:
            player5HC = 1
        try:
            player6HC = Rd3SlotModel.objects.get(player_slot = 6).player_name.HC
        except:
            player6HC = 1
        try:
            player7HC = Rd3SlotModel.objects.get(player_slot = 7).player_name.HC
        except:
            player7HC = 1
        try:
            player8HC = Rd3SlotModel.objects.get(player_slot = 8).player_name.HC
        except:
            player8HC = 1
        try:
            player9HC = Rd3SlotModel.objects.get(player_slot = 9).player_name.HC
        except:
            player9HC = 1
        try:
            player10HC = Rd3SlotModel.objects.get(player_slot = 10).player_name.HC
        except:
            player10HC = 1
        try:
            player11HC = Rd3SlotModel.objects.get(player_slot = 11).player_name.HC
        except:
            player11HC = 1
        try:
            player12HC = Rd3SlotModel.objects.get(player_slot = 12).player_name.HC
        except:
            player12HC = 1

        return (player1HC, player2HC, player3HC, player4HC, player5HC, player6HC, player7HC, player8HC, player9HC, player10HC, player11HC, player12HC)

    player1HC, player2HC, player3HC, player4HC, player5HC, player6HC, player7HC, player8HC, player9HC, player10HC, player11HC, player12HC = HC_setup()

    def stableford_conversion(par, index, HC, score):
        
        if HC >= index + 18:
            stblford_add = 2
        elif HC >= index:
            stblford_add = 1
        else:
            stblford_add = 0

        if score is None:
            score = 20        

        score_diff = par - score
        stableford_conversion = max(stblford_add + stblford_two + score_diff,0)

        return stableford_conversion

    convertedscore1 = stableford_conversion(par, index, player1HC, instance.slot1_score)
    convertedscore2 = stableford_conversion(par, index, player2HC, instance.slot2_score)
    convertedscore3 = stableford_conversion(par, index, player3HC, instance.slot3_score)
    convertedscore4 = stableford_conversion(par, index, player4HC, instance.slot4_score)
    convertedscore5 = stableford_conversion(par, index, player5HC, instance.slot5_score)
    convertedscore6 = stableford_conversion(par, index, player6HC, instance.slot6_score)
    convertedscore7 = stableford_conversion(par, index, player7HC, instance.slot7_score)
    convertedscore8 = stableford_conversion(par, index, player8HC, instance.slot8_score)
    convertedscore9 = stableford_conversion(par, index, player9HC, instance.slot9_score)
    convertedscore10 = stableford_conversion(par, index, player10HC, instance.slot10_score)
    convertedscore11 = stableford_conversion(par, index, player11HC, instance.slot11_score)
    convertedscore12 = stableford_conversion(par, index, player12HC, instance.slot12_score)
        
    stableford_scores, created = Rd3StablefordModel.objects.update_or_create(
        hole=hole,
        defaults ={
            'slot1_stbl': convertedscore1,
            'slot2_stbl': convertedscore2,
            'slot3_stbl': convertedscore3,
            'slot4_stbl': convertedscore4,
            'slot5_stbl': convertedscore5,
            'slot6_stbl': convertedscore6,
            'slot7_stbl': convertedscore7,
            'slot8_stbl': convertedscore8,
            'slot9_stbl': convertedscore9,
            'slot10_stbl': convertedscore10,
            'slot11_stbl': convertedscore11,
            'slot12_stbl': convertedscore12,
            },
        )

    player1_stablefordtotal = list(Rd3StablefordModel.objects.aggregate(Sum('slot1_stbl')).values())[0]
    player2_stablefordtotal = list(Rd3StablefordModel.objects.aggregate(Sum('slot2_stbl')).values())[0]
    player3_stablefordtotal = list(Rd3StablefordModel.objects.aggregate(Sum('slot3_stbl')).values())[0]    
    player4_stablefordtotal = list(Rd3StablefordModel.objects.aggregate(Sum('slot4_stbl')).values())[0]    
    player5_stablefordtotal = list(Rd3StablefordModel.objects.aggregate(Sum('slot5_stbl')).values())[0]    
    player6_stablefordtotal = list(Rd3StablefordModel.objects.aggregate(Sum('slot6_stbl')).values())[0]    
    player7_stablefordtotal = list(Rd3StablefordModel.objects.aggregate(Sum('slot7_stbl')).values())[0]    
    player8_stablefordtotal = list(Rd3StablefordModel.objects.aggregate(Sum('slot8_stbl')).values())[0]    
    player9_stablefordtotal = list(Rd3StablefordModel.objects.aggregate(Sum('slot9_stbl')).values())[0]    
    player10_stablefordtotal = list(Rd3StablefordModel.objects.aggregate(Sum('slot10_stbl')).values())[0]    
    player11_stablefordtotal = list(Rd3StablefordModel.objects.aggregate(Sum('slot11_stbl')).values())[0]    
    player12_stablefordtotal = list(Rd3StablefordModel.objects.aggregate(Sum('slot12_stbl')).values())[0]

    player1total, created = Rd3SlotModel.objects.update_or_create(
        player_slot=1, defaults ={'player_stbl': player1_stablefordtotal,},)

    player2total, created = Rd3SlotModel.objects.update_or_create(
        player_slot=2, defaults ={'player_stbl': player2_stablefordtotal,},)

    player3total, created = Rd3SlotModel.objects.update_or_create(
        player_slot=3, defaults ={'player_stbl': player3_stablefordtotal,},)

    player4total, created = Rd3SlotModel.objects.update_or_create(
        player_slot=4,
        defaults ={
            'player_stbl': player4_stablefordtotal,
            },
        )

    player5total, created = Rd3SlotModel.objects.update_or_create(
        player_slot=5,
        defaults ={
            'player_stbl': player5_stablefordtotal,
            },
        )

    player6total, created = Rd3SlotModel.objects.update_or_create(
        player_slot=6,
        defaults ={
            'player_stbl': player6_stablefordtotal,
            },
        )

    player7total, created = Rd3SlotModel.objects.update_or_create(
        player_slot=7,
        defaults ={
            'player_stbl': player7_stablefordtotal,
            },
        )

    player8total, created = Rd3SlotModel.objects.update_or_create(
        player_slot=8,
        defaults ={
            'player_stbl': player8_stablefordtotal,
            },
        )

    player9total, created = Rd3SlotModel.objects.update_or_create(
        player_slot=9,
        defaults ={
            'player_stbl': player9_stablefordtotal,
            },
        )

    player10total, created = Rd3SlotModel.objects.update_or_create(
        player_slot=10,
        defaults ={
            'player_stbl': player10_stablefordtotal,
            },
        )

    player11total, created = Rd3SlotModel.objects.update_or_create(
        player_slot=11,
        defaults ={
            'player_stbl': player11_stablefordtotal,
            },
        )

    player12total, created = Rd3SlotModel.objects.update_or_create(
        player_slot=12,
        defaults ={
            'player_stbl': player12_stablefordtotal,
            },
        )

@receiver(post_save, sender=Rd3ScoreModel)
def round3_callback_two(sender, instance, **kwargs):

    player1_holesplayed = Rd3ScoreModel.objects.filter(slot1_score__gt=0).count()
    player2_holesplayed = Rd3ScoreModel.objects.filter(slot2_score__gt=0).count()
    player3_holesplayed = Rd3ScoreModel.objects.filter(slot3_score__gt=0).count()
    player4_holesplayed = Rd3ScoreModel.objects.filter(slot4_score__gt=0).count()
    player5_holesplayed = Rd3ScoreModel.objects.filter(slot5_score__gt=0).count()
    player6_holesplayed = Rd3ScoreModel.objects.filter(slot6_score__gt=0).count()
    player7_holesplayed = Rd3ScoreModel.objects.filter(slot7_score__gt=0).count()
    player8_holesplayed = Rd3ScoreModel.objects.filter(slot8_score__gt=0).count()
    player9_holesplayed = Rd3ScoreModel.objects.filter(slot9_score__gt=0).count()
    player10_holesplayed = Rd3ScoreModel.objects.filter(slot10_score__gt=0).count()
    player11_holesplayed = Rd3ScoreModel.objects.filter(slot11_score__gt=0).count()
    player12_holesplayed = Rd3ScoreModel.objects.filter(slot12_score__gt=0).count()

    player1_stroketotal = list(Rd3ScoreModel.objects.aggregate(Sum('slot1_score')).values())[0]
    player2_stroketotal = list(Rd3ScoreModel.objects.aggregate(Sum('slot2_score')).values())[0]
    player3_stroketotal = list(Rd3ScoreModel.objects.aggregate(Sum('slot3_score')).values())[0]
    player4_stroketotal = list(Rd3ScoreModel.objects.aggregate(Sum('slot4_score')).values())[0]
    player5_stroketotal = list(Rd3ScoreModel.objects.aggregate(Sum('slot5_score')).values())[0]
    player6_stroketotal = list(Rd3ScoreModel.objects.aggregate(Sum('slot6_score')).values())[0]
    player7_stroketotal = list(Rd3ScoreModel.objects.aggregate(Sum('slot7_score')).values())[0]
    player8_stroketotal = list(Rd3ScoreModel.objects.aggregate(Sum('slot8_score')).values())[0]
    player9_stroketotal = list(Rd3ScoreModel.objects.aggregate(Sum('slot9_score')).values())[0]
    player10_stroketotal = list(Rd3ScoreModel.objects.aggregate(Sum('slot10_score')).values())[0]
    player11_stroketotal = list(Rd3ScoreModel.objects.aggregate(Sum('slot11_score')).values())[0]
    player12_stroketotal = list(Rd3ScoreModel.objects.aggregate(Sum('slot12_score')).values())[0]
    
    tussle_hole = Rd3HoleModel.objects.filter(tussle__isnull=False)

    tussle_sum1 = list(Rd3StablefordModel.objects.filter(hole__tussle="YES").aggregate(Sum('slot1_stbl')).values())[0]
    tussle_sum2 = list(Rd3StablefordModel.objects.filter(hole__tussle="YES").aggregate(Sum('slot2_stbl')).values())[0]
    tussle_sum3 = list(Rd3StablefordModel.objects.filter(hole__tussle="YES").aggregate(Sum('slot3_stbl')).values())[0]
    tussle_sum4 = list(Rd3StablefordModel.objects.filter(hole__tussle="YES").aggregate(Sum('slot4_stbl')).values())[0]
    tussle_sum5 = list(Rd3StablefordModel.objects.filter(hole__tussle="YES").aggregate(Sum('slot5_stbl')).values())[0]
    tussle_sum6 = list(Rd3StablefordModel.objects.filter(hole__tussle="YES").aggregate(Sum('slot6_stbl')).values())[0]
    tussle_sum7 = list(Rd3StablefordModel.objects.filter(hole__tussle="YES").aggregate(Sum('slot7_stbl')).values())[0]
    tussle_sum8 = list(Rd3StablefordModel.objects.filter(hole__tussle="YES").aggregate(Sum('slot8_stbl')).values())[0]
    tussle_sum9 = list(Rd3StablefordModel.objects.filter(hole__tussle="YES").aggregate(Sum('slot9_stbl')).values())[0]
    tussle_sum10 = list(Rd3StablefordModel.objects.filter(hole__tussle="YES").aggregate(Sum('slot10_stbl')).values())[0]
    tussle_sum11 = list(Rd3StablefordModel.objects.filter(hole__tussle="YES").aggregate(Sum('slot11_stbl')).values())[0]
    tussle_sum12 = list(Rd3StablefordModel.objects.filter(hole__tussle="YES").aggregate(Sum('slot12_stbl')).values())[0]
    
    player1total, created = Rd3SlotModel.objects.update_or_create(
        player_slot=1,
        defaults ={'player_holesplayed': player1_holesplayed, 'player_score': player1_stroketotal, 'tussle_score': tussle_sum1,},)

    player2total, created = Rd3SlotModel.objects.update_or_create(
        player_slot=2,
        defaults ={'player_holesplayed': player2_holesplayed, 'player_score': player2_stroketotal, 'tussle_score': tussle_sum2,},)

    player3total, created = Rd3SlotModel.objects.update_or_create(
        player_slot=3,
        defaults ={'player_holesplayed': player3_holesplayed, 'player_score': player3_stroketotal, 'tussle_score': tussle_sum3,},)

    player4total, created = Rd3SlotModel.objects.update_or_create(
        player_slot=4,
        defaults ={'player_holesplayed': player4_holesplayed, 'player_score': player4_stroketotal, 'tussle_score': tussle_sum4,},)

    player5total, created = Rd3SlotModel.objects.update_or_create(
        player_slot=5,
        defaults ={'player_holesplayed': player5_holesplayed, 'player_score': player5_stroketotal, 'tussle_score': tussle_sum5,},)

    player6total, created = Rd3SlotModel.objects.update_or_create(
        player_slot=6,
        defaults ={'player_holesplayed': player6_holesplayed, 'player_score': player6_stroketotal, 'tussle_score': tussle_sum6,},)

    player7total, created = Rd3SlotModel.objects.update_or_create(
        player_slot=7,
        defaults ={'player_holesplayed': player7_holesplayed, 'player_score': player7_stroketotal, 'tussle_score': tussle_sum7,},)

    player8total, created = Rd3SlotModel.objects.update_or_create(
        player_slot=8,
        defaults ={'player_holesplayed': player8_holesplayed, 'player_score': player8_stroketotal, 'tussle_score': tussle_sum8,},)

    player9total, created = Rd3SlotModel.objects.update_or_create(
        player_slot=9,
        defaults ={'player_holesplayed': player9_holesplayed, 'player_score': player9_stroketotal, 'tussle_score': tussle_sum9,},)

    player10total, created = Rd3SlotModel.objects.update_or_create(
        player_slot=10,
        defaults ={'player_holesplayed': player10_holesplayed, 'player_score': player10_stroketotal, 'tussle_score': tussle_sum10,},)

    player11total, created = Rd3SlotModel.objects.update_or_create(
        player_slot=11,
        defaults ={'player_holesplayed': player11_holesplayed, 'player_score': player11_stroketotal, 'tussle_score': tussle_sum11,},)

    player12total, created = Rd3SlotModel.objects.update_or_create(
        player_slot=12,
        defaults ={'player_holesplayed': player12_holesplayed, 'player_score': player12_stroketotal, 'tussle_score': tussle_sum12,},)
    
#RANKINGSCORES CALCS
    
    player1_stablefordtotal1 = list(Rd3StablefordModel.objects.aggregate(Sum('slot1_stbl')).values())[0]
    player2_stablefordtotal1 = list(Rd3StablefordModel.objects.aggregate(Sum('slot2_stbl')).values())[0]
    player3_stablefordtotal1 = list(Rd3StablefordModel.objects.aggregate(Sum('slot3_stbl')).values())[0]    
    player4_stablefordtotal1 = list(Rd3StablefordModel.objects.aggregate(Sum('slot4_stbl')).values())[0]    
    player5_stablefordtotal1 = list(Rd3StablefordModel.objects.aggregate(Sum('slot5_stbl')).values())[0]    
    player6_stablefordtotal1 = list(Rd3StablefordModel.objects.aggregate(Sum('slot6_stbl')).values())[0]    
    player7_stablefordtotal1 = list(Rd3StablefordModel.objects.aggregate(Sum('slot7_stbl')).values())[0]    
    player8_stablefordtotal1 = list(Rd3StablefordModel.objects.aggregate(Sum('slot8_stbl')).values())[0]    
    player9_stablefordtotal1 = list(Rd3StablefordModel.objects.aggregate(Sum('slot9_stbl')).values())[0]    
    player10_stablefordtotal1 = list(Rd3StablefordModel.objects.aggregate(Sum('slot10_stbl')).values())[0]    
    player11_stablefordtotal1 = list(Rd3StablefordModel.objects.aggregate(Sum('slot11_stbl')).values())[0]    
    player12_stablefordtotal1 = list(Rd3StablefordModel.objects.aggregate(Sum('slot12_stbl')).values())[0]

    try:
        player1_rankscore = player1_stablefordtotal1/player1_holesplayed
    except:
        player1_rankscore = 0
    try:
        player2_rankscore = player2_stablefordtotal1/player2_holesplayed
    except:
        player2_rankscore = 0
    try:
        player3_rankscore = player3_stablefordtotal1/player3_holesplayed
    except:
        player3_rankscore = 0
    try:
        player4_rankscore = player4_stablefordtotal1/player4_holesplayed
    except:
        player4_rankscore = 0
    try:
        player5_rankscore = player5_stablefordtotal1/player5_holesplayed
    except:
        player5_rankscore = 0
    try:
        player6_rankscore = player6_stablefordtotal1/player6_holesplayed
    except:
        player6_rankscore = 0
    try:
        player7_rankscore = player7_stablefordtotal1/player7_holesplayed
    except:
        player7_rankscore = 0
    try:
        player8_rankscore = player8_stablefordtotal1/player8_holesplayed
    except:
        player8_rankscore = 0
    try:
        player9_rankscore = player9_stablefordtotal1/player9_holesplayed
    except:
        player9_rankscore = 0
    try:
        player10_rankscore = player10_stablefordtotal1/player10_holesplayed
    except:
        player10_rankscore = 0
    try:
        player11_rankscore = player11_stablefordtotal1/player11_holesplayed
    except:
        player11_rankscore = 0
    try:
        player12_rankscore = player12_stablefordtotal1/player12_holesplayed
    except:
        player12_rankscore = 0

    player1total, created = Rd3SlotModel.objects.update_or_create(
        player_slot=1, defaults ={'player_rankscore': player1_rankscore,},)
    player2total, created = Rd3SlotModel.objects.update_or_create(
        player_slot=2, defaults ={'player_rankscore': player2_rankscore,},)
    player3total, created = Rd3SlotModel.objects.update_or_create(
        player_slot=3, defaults ={'player_rankscore': player3_rankscore,},)
    player4total, created = Rd3SlotModel.objects.update_or_create(
        player_slot=4, defaults ={'player_rankscore': player4_rankscore,},)
    player5total, created = Rd3SlotModel.objects.update_or_create(
        player_slot=5, defaults ={'player_rankscore': player5_rankscore,},)
    player6total, created = Rd3SlotModel.objects.update_or_create(
        player_slot=6, defaults ={'player_rankscore': player6_rankscore,},)
    player7total, created = Rd3SlotModel.objects.update_or_create(
        player_slot=7, defaults ={'player_rankscore': player7_rankscore,},)
    player8total, created = Rd3SlotModel.objects.update_or_create(
        player_slot=8, defaults ={'player_rankscore': player8_rankscore,},)
    player9total, created = Rd3SlotModel.objects.update_or_create(
        player_slot=9, defaults ={'player_rankscore': player9_rankscore,},)
    player10total, created = Rd3SlotModel.objects.update_or_create(
        player_slot=10, defaults ={'player_rankscore': player10_rankscore,},)
    player11total, created = Rd3SlotModel.objects.update_or_create(
        player_slot=11, defaults ={'player_rankscore': player11_rankscore,},)
    player12total, created = Rd3SlotModel.objects.update_or_create(
        player_slot=12, defaults ={'player_rankscore': player12_rankscore,},)

## -- END ROUND 3 -- ##

class SportsTippingModel(models.Model):
    name = models.ForeignKey('PlayerModel',on_delete = models.CASCADE)
    password = models.CharField(max_length=30, blank=True, null=True)
    game1 = models.CharField(max_length=20,choices=GAME_1,blank=True, null=True)
    game2 = models.CharField(max_length=20,choices=GAME_2,blank=True, null=True)
    game3 = models.CharField(max_length=20,choices=GAME_3,blank=True, null=True)
    game4 = models.CharField(max_length=20,choices=GAME_4,blank=True, null=True)
    game5 = models.CharField(max_length=20,choices=GAME_5,blank=True, null=True)
    game6 = models.CharField(max_length=20,choices=GAME_6,blank=True, null=True)
    game7 = models.CharField(max_length=20,choices=GAME_7,blank=True, null=True)
    game8 = models.CharField(max_length=20,choices=GAME_8,blank=True, null=True)
    game9 = models.CharField(max_length=20,choices=GAME_9,blank=True, null=True)
    game10 = models.CharField(max_length=20,choices=GAME_10,blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)

@receiver(post_save, sender=SportsTippingModel)
def send_to_scores(sender, instance, **kwargs):
    submissions = SportsTippingModel.objects.all()
    
    for x in submissions:
        addition_playerdeets = SportsTippingScoreModel.objects.update_or_create(name=x.name, defaults={'time': x.time,},)

class SportsTippingResultsModel(models.Model):
    name = models.CharField(max_length=20,default="result", blank=True, null=True)
    result1 = models.CharField(max_length=20,choices=GAME_1R,blank=True, null=True)
    result2 = models.CharField(max_length=20,choices=GAME_2R,blank=True, null=True)
    result3 = models.CharField(max_length=20,choices=GAME_3R,blank=True, null=True)
    result4 = models.CharField(max_length=20,choices=GAME_4R,blank=True, null=True)
    result5 = models.CharField(max_length=20,choices=GAME_5R,blank=True, null=True)
    result6 = models.CharField(max_length=20,choices=GAME_6R,blank=True, null=True)
    result7 = models.CharField(max_length=20,choices=GAME_7R,blank=True, null=True)
    result8 = models.CharField(max_length=20,choices=GAME_8R,blank=True, null=True)
    result9 = models.CharField(max_length=20,choices=GAME_9R,blank=True, null=True)
    result10 = models.CharField(max_length=20,choices=GAME_10R,blank=True, null=True)

@receiver(post_save, sender=SportsTippingResultsModel)
def send_to_scores2(sender, instance, **kwargs):
    submissions = SportsTippingModel.objects.all()
    results = SportsTippingResultsModel.objects.get(name='result')
    result1 = results.result1
    result2 = results.result2
    result3 = results.result3
    result4 = results.result4
    result5 = results.result5
    result6 = results.result6
    result7 = results.result7
    result8 = results.result8
    result9 = results.result9
    result10 = results.result10

    for x in submissions:
        tip1 = x.game1
        tip2 = x.game2
        tip3 = x.game3
        tip4 = x.game4
        tip5 = x.game5
        tip6 = x.game6
        tip7 = x.game7
        tip8 = x.game8
        tip9 = x.game9
        tip10 = x.game10

        def total_tips():
            if tip1 == result1:
                outcome1 = 1
            else:
                outcome1=0
            if tip2 == result2:
                outcome2 = 1
            else:
                outcome2 = 0
            if tip3 == result3:
                outcome3 = 1
            else:
                outcome3 = 0
            if tip4 == result4:
                outcome4 = 1
            else:
                outcome4 = 0
            if tip5 == result5:
                outcome5 = 1
            else:
                outcome5 = 0
            if tip6 == result6:
                outcome6 = 1
            else:
                outcome6 = 0
            if tip7 == result7:
                outcome7 = 1
            else:
                outcome7 = 0
            if tip8 == result8:
                outcome8 = 1
            else:
                outcome8 = 0
            if tip9 == result9:
                outcome9 = 1
            else:
                outcome9 = 0
            if tip10 == result10:
                outcome10 = 1
            else:
                outcome10 = 0
                
            total = outcome1 + outcome2 + outcome3 + outcome4 + outcome5 + outcome6 + outcome7 + outcome8 + outcome9 + outcome10

            return total

        total = total_tips()
        
        addition = SportsTippingScoreModel.objects.update_or_create(name=x.name, defaults={'total': total,},)

class SportsTippingScoreModel(models.Model):
    name = models.ForeignKey('PlayerModel',on_delete = models.CASCADE)
    time = models.DateTimeField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['-total', 'time']

class FridaySocialModel(models.Model):
    name = models.ForeignKey('PlayerModel',on_delete = models.CASCADE)
    password = models.CharField(max_length=30, blank=True, null=True)
    best = models.ForeignKey('PlayerModel',related_name='fri_best', on_delete = models.CASCADE)
    honorable = models.ForeignKey('PlayerModel',related_name='fri_honorable',on_delete = models.CASCADE)

class SaturdaySocialModel(models.Model):
    name = models.ForeignKey('PlayerModel',on_delete = models.CASCADE)
    password = models.CharField(max_length=30, blank=True, null=True)
    best = models.ForeignKey('PlayerModel',related_name='sat_best', on_delete = models.CASCADE)
    honorable = models.ForeignKey('PlayerModel',related_name='sat_honorable',on_delete = models.CASCADE)

class TourAgendaModel(models.Model):
    day = models.CharField(max_length=10,choices=DAYS,blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    time = models.CharField(max_length=40,blank=True, null=True)
    event = models.CharField(max_length=40,blank=True, null=True)
    location = models.CharField(max_length=40,blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)
    total_points = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['number']
    
class TopGolfModel(models.Model):
    reference = models.CharField(max_length=20, default="reference", blank=True, null=True)
    first = models.ForeignKey('PlayerModel',related_name='firstTopGolf', on_delete = models.CASCADE, blank=True, null=True)
    second = models.ForeignKey('PlayerModel',related_name='secondTopGolf', on_delete = models.CASCADE, blank=True, null=True)
    third = models.ForeignKey('PlayerModel',related_name='thirdTopGolf', on_delete = models.CASCADE, blank=True, null=True)
    fourth = models.ForeignKey('PlayerModel',related_name='fourthTopGolf', on_delete = models.CASCADE, blank=True, null=True)
    fifth = models.ForeignKey('PlayerModel',related_name='fifthTopGolf', on_delete = models.CASCADE, blank=True, null=True)
    sixth = models.ForeignKey('PlayerModel',related_name='sixthTopGolf', on_delete = models.CASCADE, blank=True, null=True)

class RacingModel(models.Model):
    reference = models.CharField(max_length=20, default="reference", blank=True, null=True)
    first = models.ForeignKey('PlayerModel',related_name='firstRacing', on_delete = models.CASCADE, blank=True, null=True)
    second = models.ForeignKey('PlayerModel',related_name='secondRacing', on_delete = models.CASCADE, blank=True, null=True)
    third = models.ForeignKey('PlayerModel',related_name='thirdRacing', on_delete = models.CASCADE, blank=True, null=True)
    fourth = models.ForeignKey('PlayerModel',related_name='fourthRacing', on_delete = models.CASCADE, blank=True, null=True)
    fifth = models.ForeignKey('PlayerModel',related_name='fifthRacing', on_delete = models.CASCADE, blank=True, null=True)
    sixth = models.ForeignKey('PlayerModel',related_name='sixthRacing', on_delete = models.CASCADE, blank=True, null=True)

