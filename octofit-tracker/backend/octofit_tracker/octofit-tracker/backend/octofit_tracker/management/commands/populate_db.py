from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Limpa dados existentes
        User = get_user_model()
        User.objects.all().delete()
        Team = app_models.Team
        Team.objects.all().delete()
        Activity = app_models.Activity
        Activity.objects.all().delete()
        Leaderboard = app_models.Leaderboard
        Leaderboard.objects.all().delete()
        Workout = app_models.Workout
        Workout.objects.all().delete()

        # Cria times
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Cria usuários
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='1234', team=marvel)
        hulk = User.objects.create_user(username='hulk', email='hulk@marvel.com', password='1234', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='1234', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='1234', team=dc)

        # Cria atividades
        Activity.objects.create(user=ironman, type='run', duration=30, distance=5)
        Activity.objects.create(user=hulk, type='walk', duration=60, distance=4)
        Activity.objects.create(user=batman, type='cycle', duration=45, distance=15)
        Activity.objects.create(user=superman, type='swim', duration=50, distance=2)

        # Cria workouts
        Workout.objects.create(name='Treino Marvel', description='Treino para heróis Marvel', team=marvel)
        Workout.objects.create(name='Treino DC', description='Treino para heróis DC', team=dc)

        # Cria leaderboard
        Leaderboard.objects.create(user=ironman, points=100)
        Leaderboard.objects.create(user=hulk, points=80)
        Leaderboard.objects.create(user=batman, points=90)
        Leaderboard.objects.create(user=superman, points=95)

        self.stdout.write(self.style.SUCCESS('Banco populado com dados de teste!'))
