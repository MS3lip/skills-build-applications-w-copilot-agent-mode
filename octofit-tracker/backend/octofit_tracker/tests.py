from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Equipe Teste")
        self.assertEqual(str(team), "Equipe Teste")

    def test_create_user(self):
        team = Team.objects.create(name="Equipe User")
        user = User.objects.create_user(username="usuario", email="u@t.com", password="senha", team=team)
        self.assertEqual(user.team, team)

    def test_create_activity(self):
        team = Team.objects.create(name="Equipe Atividade")
        user = User.objects.create_user(username="atividade", email="a@t.com", password="senha", team=team)
        activity = Activity.objects.create(user=user, type="corrida", duration=30, distance=5.0)
        self.assertEqual(str(activity), "atividade - corrida")

    def test_create_workout(self):
        team = Team.objects.create(name="Equipe Workout")
        workout = Workout.objects.create(name="Treino 1", description="Desc", team=team)
        self.assertEqual(str(workout), "Treino 1")

    def test_create_leaderboard(self):
        team = Team.objects.create(name="Equipe Leader")
        user = User.objects.create_user(username="leader", email="l@t.com", password="senha", team=team)
        leaderboard = Leaderboard.objects.create(user=user, points=100)
        self.assertEqual(str(leaderboard), "leader: 100")
