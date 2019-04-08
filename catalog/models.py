from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from catalog.choices import *
from django.db.models import Sum, Count
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class PlayerModel(models.Model):
    name = models.CharField(max_length=30)
    HC = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='playerimages', blank=True, null=True)
    jacket = models.CharField(max_length=10,choices=YES_NO,blank=True, null=True)

    def __str__(self):
        return self.name

#ROUND 1
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

    class Meta:
        ordering = ['-player_rankscore', 'player_name__HC']


class Rd1ScoreModel(models.Model):
    hole = models.ForeignKey('Rd1HoleModel', on_delete = models.CASCADE)
    ctp = models.ForeignKey('PlayerModel', related_name="ctp", on_delete = models.CASCADE, blank=True, null=True)
    ld = models.ForeignKey('PlayerModel', related_name="ld", on_delete = models.CASCADE, blank=True, null=True)
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
        defaults ={
            'player_stbl': player4_stablefordtotal,
            },
        )

    player5total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=5,
        defaults ={
            'player_stbl': player5_stablefordtotal,
            },
        )

    player6total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=6,
        defaults ={
            'player_stbl': player6_stablefordtotal,
            },
        )

    player7total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=7,
        defaults ={
            'player_stbl': player7_stablefordtotal,
            },
        )

    player8total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=8,
        defaults ={
            'player_stbl': player8_stablefordtotal,
            },
        )

    player9total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=9,
        defaults ={
            'player_stbl': player9_stablefordtotal,
            },
        )

    player10total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=10,
        defaults ={
            'player_stbl': player10_stablefordtotal,
            },
        )

    player11total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=11,
        defaults ={
            'player_stbl': player11_stablefordtotal,
            },
        )

    player12total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=12,
        defaults ={
            'player_stbl': player12_stablefordtotal,
            },
        )

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

    player1total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=1,
        defaults ={
            'player_holesplayed': player1_holesplayed,
            },
        )

    player2total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=2,
        defaults ={
            'player_holesplayed': player2_holesplayed,            
            },
        )

    player3total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=3,
        defaults ={
            'player_holesplayed': player3_holesplayed,
            },
        )

    player4total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=4,
        defaults ={
            'player_holesplayed': player4_holesplayed,
            },
        )

    player5total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=5,
        defaults ={
            'player_holesplayed': player5_holesplayed,
            },
        )

    player6total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=6,
        defaults ={
            'player_holesplayed': player6_holesplayed,
            },
        )

    player7total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=7,
        defaults ={
            'player_holesplayed': player7_holesplayed,
            },
        )

    player8total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=8,
        defaults ={
            'player_holesplayed': player8_holesplayed,
            },
        )

    player9total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=9,
        defaults ={
            'player_holesplayed': player9_holesplayed,
            },
        )

    player10total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=10,
        defaults ={
            'player_holesplayed': player10_holesplayed,
            },
        )

    player11total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=11,
        defaults ={
            'player_holesplayed': player11_holesplayed,
            },
        )

    player12total, created = Rd1SlotModel.objects.update_or_create(
        player_slot=12,
        defaults ={
            'player_holesplayed': player12_holesplayed,
            },
        )
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
        player1_rankscore = None
    try:
        player2_rankscore = player2_stablefordtotal1/player2_holesplayed
    except:
        player2_rankscore = None
    try:
        player3_rankscore = player3_stablefordtotal1/player3_holesplayed
    except:
        player3_rankscore = None
    try:
        player4_rankscore = player4_stablefordtotal1/player4_holesplayed
    except:
        player4_rankscore = None
    try:
        player5_rankscore = player5_stablefordtotal1/player5_holesplayed
    except:
        player5_rankscore = None
    try:
        player6_rankscore = player6_stablefordtotal1/player6_holesplayed
    except:
        player6_rankscore = None
    try:
        player7_rankscore = player7_stablefordtotal1/player7_holesplayed
    except:
        player7_rankscore = None
    try:
        player8_rankscore = player1_stablefordtotal1/player8_holesplayed
    except:
        player8_rankscore = None
    try:
        player9_rankscore = player9_stablefordtotal1/player9_holesplayed
    except:
        player9_rankscore = None
    try:
        player10_rankscore = player10_stablefordtotal1/player10_holesplayed
    except:
        player10_rankscore = None
    try:
        player11_rankscore = player11_stablefordtotal1/player11_holesplayed
    except:
        player11_rankscore = None
    try:
        player12_rankscore = player12_stablefordtotal1/player12_holesplayed
    except:
        player12_rankscore = None

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

class Rd1CTPModel(models.Model):
    CTPnumber = models.IntegerField(primary_key=True)
    number = models.ForeignKey('Rd1HoleModel',on_delete = models.CASCADE, blank=True, null=True)
    winner = models.ForeignKey('PlayerModel',on_delete = models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ['CTPnumber']

class SportsTippingModel(models.Model):
    name = models.ForeignKey('PlayerModel',on_delete = models.CASCADE)
    tip1 = models.CharField(max_length=10,choices=YES_NO,blank=True, null=True)