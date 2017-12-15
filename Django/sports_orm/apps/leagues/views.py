from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"11": League.objects.filter(sport="Baseball"),
		"l2": League.objects.filter(name__contains="Women"),
		"l3": League.objects.filter(sport__contains="Hockey"),
		"l4": League.objects.exclude(sport="Football"),
		"l5": League.objects.filter(name__contains="Conference"),
		"l6": League.objects.filter(name__contains="Atlantic"),
		"t1": Team.objects.filter(location="Dallas"),
		"t2": Team.objects.filter(team_name__contains="Raptors"),
		"t3": Team.objects.filter(location__contains="City"),
		"t4": Team.objects.filter(team_name__startswith="T"),
		"t5": Team.objects.order_by("location"),
		"t6": Team.objects.order_by("-team_name"),
		"p1": Player.objects.filter(last_name="Cooper"),
		"p2": Player.objects.filter(first_name="Joshua"),
		"p3": Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua"),
		"p4": Player.objects.filter(first_name="Alexander")|Player.objects.filter(first_name="Wyatt"),

		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
	}
	
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")