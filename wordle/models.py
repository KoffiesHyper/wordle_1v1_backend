from django.db import models

# Create your models here.

class Player(models.Model):
    tag = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.tag

class Match(models.Model):
    players = models.ManyToManyField('Player')
    player_count = models.IntegerField()
    boards = models.JSONField(default={})
    has_started = models.BooleanField(default=False)
    to_guess = models.CharField(max_length=12, blank=True)

    def add_player(self, newPlayer):
        if newPlayer not in self.players.all():
            self.players.add(newPlayer)
            self.save()