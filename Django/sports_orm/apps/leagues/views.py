from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count

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

		"t21": League.objects.get(name="Atlantic Soccer Conference").teams.all(),
		"p21": Team.objects.get(team_name="Penguins", location="Boston").curr_players.all(),
		"p22": Player.objects.filter(curr_team__league__name="International Collegiate Baseball Conference"),
		"p23": Player.objects.filter(curr_team__league__name="American Conference of Amateur Football").filter(last_name="Lopez"),
		"p24": Player.objects.filter(curr_team__league__sport="Football"),
		"t22": Team.objects.filter(curr_players__first_name="Sophia"),
		"l21": League.objects.filter(teams__curr_players__first_name="Sophia"),
		"p25": Player.objects.filter(last_name="Flores").exclude(curr_team__team_name="Roughriders"),
		"t23": Team.objects.filter(all_players__first_name="Samuel", all_players__last_name="Evans"),
		"p26": Player.objects.filter(all_teams__team_name="Tiger-Cats"),
		"p27": Player.objects.filter(all_teams__team_name="Vikings", all_teams__location="Wichita").exclude(curr_team__team_name="Vikings", curr_team__location="Wichita"),
		"t24": Team.objects.filter(all_players__first_name="Jacob", all_players__last_name="Gray").exclude(location="Oregon"),
		"p28": Player.objects.filter(all_teams__league__name="Atlantic Federation of Amateur Baseball Players").filter(first_name="Joshua"),
		"t25": Team.objects.annotate(player_count=Count('all_players')).filter(player_count__gte=12),
		"p29": Player.objects.annotate(team_count=Count('all_teams')).order_by("team_count"),
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