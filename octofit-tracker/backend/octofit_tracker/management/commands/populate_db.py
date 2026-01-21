from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker import models as app_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        app_models.Team.objects.all().delete()
        app_models.Activity.objects.all().delete()
        app_models.Leaderboard.objects.all().delete()
        app_models.Workout.objects.all().delete()
        User.objects.all().delete()

        marvel = app_models.Team.objects.create(name='Marvel')
        dc = app_models.Team.objects.create(name='DC')

        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='1234', team=marvel)
        hulk = User.objects.create_user(username='hulk', email='hulk@marvel.com', password='1234', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='1234', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='1234', team=dc)

        app_models.Activity.objects.create(user=ironman, type='run', duration=30, distance=5)
        app_models.Activity.objects.create(user=hulk, type='walk', duration=60, distance=4)
        app_models.Activity.objects.create(user=batman, type='cycle', duration=45, distance=15)
        app_models.Activity.objects.create(user=superman, type='swim', duration=50, distance=2)

        app_models.Workout.objects.create(name='Treino Marvel', description='Treino para heróis Marvel', team=marvel)
        app_models.Workout.objects.create(name='Treino DC', description='Treino para heróis DC', team=dc)

        app_models.Leaderboard.objects.create(user=ironman, points=100)
        app_models.Leaderboard.objects.create(user=hulk, points=80)
        app_models.Leaderboard.objects.create(user=batman, points=90)
        app_models.Leaderboard.objects.create(user=superman, points=95)

        self.stdout.write(self.style.SUCCESS('Banco populado com dados de teste!'))
