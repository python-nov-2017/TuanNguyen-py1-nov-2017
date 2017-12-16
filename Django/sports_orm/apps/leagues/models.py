from django.db import models

class League(models.Model):
	name = models.CharField(max_length=50)
	sport = models.CharField(max_length=15)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __repr__(self):
		return "<League Object: {}>".format(self.name)
class Team(models.Model):
	location = models.CharField(max_length=50)
	team_name = models.CharField(max_length=50)
	league = models.ForeignKey(League, related_name="teams")
	def __repr__(self):
		return "<Team Object: {}>".format(self.team_name)

class Player(models.Model):
	first_name = models.CharField(max_length=15)
	last_name = models.CharField(max_length=15)
	curr_team = models.ForeignKey(Team, related_name="curr_players")
	all_teams = models.ManyToManyField(Team, related_name="all_players")
	def __repr__(self):
		return "<Player Object: {} {}>".format(self.first_name, self.last_name)
