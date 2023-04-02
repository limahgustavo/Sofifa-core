from django.db import models


class Player(models.Model):
    sofifa_id = models.IntegerField(
        db_column='nb_sofifa_id',
        null=False,
        verbose_name='Sofifa id'
    )
    player_url = models.CharField(
        db_column='tx_player_url',
        verbose_name='Player url',
        max_length=128,
        null=False
    )
    short_name = models.CharField(
        db_column='tx_short_name',
        verbose_name='Short name',
        max_length=64,
        null=False
    )
    long_name = models.CharField(
        db_column='tx_long_name',
        verbose_name='Long name',
        max_length=64,
        null=False
    )
    age = models.IntegerField(
        db_column='nb_agr',
        null=False,
        verbose_name='Age'
    )
    nationality = models.CharField(
        db_column='tx_nationality',
        verbose_name='Nationality',
        max_length=64,
        null=False
    )
    club_name = models.CharField(
        db_column='tx_club_name',
        verbose_name='Club name',
        max_length=64,
        null=False
    )
    league_name = models.CharField(
        db_column='tx_league_name',
        verbose_name='League name',
        max_length=64,
        null=False
    )
    overall = models.IntegerField(
        db_column='nb_overall',
        null=False,
        verbose_name='Overall'
    )
    potential = models.IntegerField(
        db_column='nb_potential',
        null=False,
        verbose_name='Potential'
    )

    class Meta:
        managed = True
        db_table = 'player'
        verbose_name = 'Player'
        verbose_name_plural = 'Players'
