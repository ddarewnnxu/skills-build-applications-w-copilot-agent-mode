from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # 清空所有資料
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # 建立隊伍
        marvel = Team.objects.create(name='marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='dc', description='DC Superheroes')

        # 建立使用者
        users = [
            User(name='Tony Stark', email='tony@marvel.com', team='marvel', is_superhero=True),
            User(name='Steve Rogers', email='steve@marvel.com', team='marvel', is_superhero=True),
            User(name='Bruce Wayne', email='bruce@dc.com', team='dc', is_superhero=True),
            User(name='Clark Kent', email='clark@dc.com', team='dc', is_superhero=True),
        ]
        for user in users:
            user.save()

        # 建立活動
        Activity.objects.create(user=users[0], type='run', duration=30, calories=300, date='2026-01-01')
        Activity.objects.create(user=users[1], type='swim', duration=45, calories=400, date='2026-01-02')
        Activity.objects.create(user=users[2], type='cycle', duration=60, calories=500, date='2026-01-03')
        Activity.objects.create(user=users[3], type='walk', duration=20, calories=100, date='2026-01-04')

        # 建立排行榜
        Leaderboard.objects.create(team=marvel, points=1500, rank=1)
        Leaderboard.objects.create(team=dc, points=1200, rank=2)

        # 建立訓練
        Workout.objects.create(name='Pushups', description='Upper body strength', suggested_for='marvel')
        Workout.objects.create(name='Squats', description='Lower body strength', suggested_for='dc')

        self.stdout.write(self.style.SUCCESS('octofit_db 已成功填充測試資料！'))
