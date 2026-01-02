from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(name='Clark Kent', email='clark@dc.com', team='dc', is_superhero=True)
        self.assertEqual(user.name, 'Clark Kent')
        self.assertTrue(user.is_superhero)

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='marvel', description='Marvel Superheroes')
        self.assertEqual(team.name, 'marvel')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team='dc', is_superhero=True)
        activity = Activity.objects.create(user=user, type='run', duration=30, calories=300, date='2026-01-01')
        self.assertEqual(activity.type, 'run')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='dc', description='DC Superheroes')
        leaderboard = Leaderboard.objects.create(team=team, points=1000, rank=1)
        self.assertEqual(leaderboard.rank, 1)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Upper body', suggested_for='marvel')
        self.assertEqual(workout.name, 'Pushups')
