from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def setUp(self):
        User.objects.create(username="testuser", email="testuser@example.com", password="password123")

    def test_user_creation(self):
        user = User.objects.get(username="testuser")
        self.assertEqual(user.email, "testuser@example.com")

class TeamModelTest(TestCase):
    def setUp(self):
        team = Team.objects.create(name="Test Team")
        user = User.objects.create(username="teamuser", email="teamuser@example.com", password="password123")
        team.members.add(user)

    def test_team_creation(self):
        team = Team.objects.get(name="Test Team")
        self.assertEqual(team.members.count(), 1)

class ActivityModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(username="activityuser", email="activityuser@example.com", password="password123")
        Activity.objects.create(user=user, activity_type="Running", duration="01:00:00")

    def test_activity_creation(self):
        activity = Activity.objects.get(activity_type="Running")
        self.assertEqual(activity.duration, "01:00:00")

class LeaderboardModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(username="leaderboarduser", email="leaderboarduser@example.com", password="password123")
        Leaderboard.objects.create(user=user, score=100)

    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.get(score=100)
        self.assertEqual(leaderboard.user.username, "leaderboarduser")

class WorkoutModelTest(TestCase):
    def setUp(self):
        Workout.objects.create(name="Test Workout", description="A test workout description")

    def test_workout_creation(self):
        workout = Workout.objects.get(name="Test Workout")
        self.assertEqual(workout.description, "A test workout description")