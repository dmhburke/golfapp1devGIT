from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Sum, Count
from django.views import generic
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Add models here
from catalog.models import Rd1HoleModel, PlayerModel, Rd1SlotModel, Rd1ScoreModel, Rd1StablefordModel, EventEntryModel, LeaderBoardModel, SportsTippingModel,FridaySocialModel 
# Add forms here
from catalog.forms import Rd1ScoreForm, SportsTippingForm, FridaySocialForm, SaturdaySocialForm

#from catalog.signals import *

def login (request):
    """View function for login of site."""
    # Define views here    
    context = {}
    return render(request, 'login.html', context=context)

def landingpage (request):
    """View function for login of site."""
    # Define views here    
    context = {}
    return render(request, 'landingPage.html', context=context)

def fullleaderboard (request):
    """Define function for leaderboard view"""
    # Define views here
    score_submit = EventEntryModel.objects.exclude(winner__isnull=True).count()
    active_players = PlayerModel.objects.all()
    
    context = {
    'score_submit': score_submit,
    'active_players': active_players,
    }

    return render(request, 'fullLeaderboard.html', context=context)

def scoringpage (request):
    """View function for login of site."""
    # Define views here    
    context = {}
    return render(request, 'scoringPage.html', context=context)

class rd1holelist (generic.ListView):
    """Create list of holes"""
    model = Rd1HoleModel
    template_name = 'rd1HoleList.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in additional querysets for context
        ctp_hole = Rd1HoleModel.objects.filter(CTP__gt=0)
        ld_hole = Rd1HoleModel.objects.filter(LD__gt=0)
        tussle_hole = Rd1HoleModel.objects.filter(tussle__isnull=False)

        context['ctp_hole'] = ctp_hole
        context['ld_hole'] = ld_hole
        return context

def rd1holedetail(request,pk):
    """Create hole detail for score entry"""
    #Hole details
    hole_number = Rd1HoleModel.objects.get(pk=pk).number
    hole_index = Rd1HoleModel.objects.get(pk=pk).index
    hole_par = Rd1HoleModel.objects.get(pk=pk).par
    hole_ctp = Rd1HoleModel.objects.get(pk=pk).CTP
    hole_ld = Rd1HoleModel.objects.get(pk=pk).LD
    selected_hole = Rd1HoleModel.objects.get(number=pk)

    
    #Count active players for dynamic loading
    active_players = Rd1SlotModel.objects.filter(player_name__isnull=False).count()

    #Assign players to slots
    def player_setup():
        try:
            player1 = Rd1SlotModel.objects.get(player_slot = 1)
        except:
            player1 = 'None'
        try:
            player2 = Rd1SlotModel.objects.get(player_slot = 2)
        except:
            player2 = 'None'
        try:
            player3 = Rd1SlotModel.objects.get(player_slot = 3)
        except:
            player3 = 'None'
        try:
            player4 = Rd1SlotModel.objects.get(player_slot = 4)
        except:
            player4 = 'None'
        try:
            player5 = Rd1SlotModel.objects.get(player_slot = 5)
        except:
            player5 = 'None'
        try:
            player6 = Rd1SlotModel.objects.get(player_slot = 6)
        except:
            player6 = 'None'
        try:
            player7 = Rd1SlotModel.objects.get(player_slot = 7)
        except:
            player7 = 'None'
        try:
            player8 = Rd1SlotModel.objects.get(player_slot = 8)
        except:
            player8 = 'None'
        try:
            player9 = Rd1SlotModel.objects.get(player_slot = 9)
        except:
            player9 = 'None'
        try:
            player10 = Rd1SlotModel.objects.get(player_slot = 10)
        except:
            player10 = 'None'
        try:
            player11 = Rd1SlotModel.objects.get(player_slot = 11)
        except:
            player11 = 'None'
        try:
            player12 = Rd1SlotModel.objects.get(player_slot = 12)
        except:
            player12 = 'None'

        return (player1, player2, player3, player4, player5, player6, player7, player8, player9, player10, player11, player12)

    player1, player2, player3, player4, player5, player6, player7, player8, player9, player10, player11, player12 = player_setup()

    #Accept form input (create, edit, display)
    if request.method == 'POST':
        form = Rd1ScoreForm(request.POST)
        try:
            instance = Rd1ScoreModel.objects.get(hole=selected_hole)
            instance.ctp = form.save(commit=False).ctp
            instance.ld = form.save(commit=False).ld
            instance.slot1_score = form.save(commit=False).slot1_score
            instance.slot2_score = form.save(commit=False).slot2_score
            instance.slot3_score = form.save(commit=False).slot3_score
            instance.slot4_score = form.save(commit=False).slot4_score
            instance.slot5_score = form.save(commit=False).slot5_score
            instance.slot6_score = form.save(commit=False).slot6_score
            instance.slot7_score = form.save(commit=False).slot7_score
            instance.slot8_score = form.save(commit=False).slot8_score
            instance.slot9_score = form.save(commit=False).slot9_score
            instance.slot10_score = form.save(commit=False).slot10_score
            instance.slot11_score = form.save(commit=False).slot11_score
            instance.slot12_score = form.save(commit=False).slot12_score
            instance.save()
            return redirect('rd1holelist')
        except:
            if form.is_valid():
                post = form.save(commit=False)
                post.hole = selected_hole
                post.save()
                return redirect('rd1holelist')
    else:
        try:
            form = Rd1ScoreForm(instance=get_object_or_404(Rd1ScoreModel,hole=selected_hole))
        except:
            form = Rd1ScoreForm()

    
    # Define HTML context
    context = {
        'hole_number': hole_number,
        'hole_index': hole_index,
        'hole_par': hole_par,
        'active_players': active_players,
        'player1': player1,
        'player2': player2,
        'player3': player3,
        'player4': player4,
        'player5': player5,
        'player6': player6,
        'player7': player7,
        'player8': player8,
        'player9': player9,
        'player10': player10,
        'player11': player11,
        'player12': player12,
        'form': form,
        'hole_ctp': hole_ctp,
        'hole_ld': hole_ld,
        }

    return render(request, 'rd1HoleDetail.html', context=context)

def rd1leaderboard(request):
    """Create leaderboard view for Round1"""

    #Add views
    playing_players = Rd1SlotModel.objects.filter(player_name__isnull=False)

    #Add context
    context = {
        'playing_players': playing_players,
        }

    return render(request, 'rd1Leaderboard.html', context=context)

def entertips(request):
    """Create view for tips entry view"""

    #Add views
    if request.method == 'POST':        
        form = SportsTippingForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('entertips')        

    else:
        form = SportsTippingForm()
    
    context = {
        'form': form,
        }

    return render(request, 'enterTips.html', context=context)

def entersocial(request):
    """Create view for social entry view"""

    if request.method == 'POST':
        if 'friday' in request.POST:
            fridayform = FridaySocialForm(request.POST, prefix='friday')
            if fridayform.is_valid():
                post = fridayform.save(commit=False)
                post.save()
                return redirect('landingpage')
                saturdayform = SaturdaySocialForm(prefix='saturday')

        elif 'saturday' in request.POST:
            saturdayform = SaturdaySocialForm(request.POST, prefix='saturday')
            if saturdayform.is_valid():
                post = saturdayform.save(commit=False)
                post.save()
                return redirect('landingpage')
                fridayform = FridaySocialForm(prefix='friday')
    else:
        fridayform = FridaySocialForm(prefix='friday')
        saturdayform = SaturdaySocialForm(prefix='saturday')
    
    context = {
#        'fridayform': fridayform,
        'saturdayform': saturdayform,
        'fridayform': fridayform,
        }
    
    return render(request, 'enterSocial.html', context=context)
