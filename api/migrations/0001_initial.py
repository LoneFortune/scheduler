# Generated by Django 3.0.4 on 2020-03-19 19:49

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('skill', models.IntegerField(default=None, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Skill')),
                ('notes', models.TextField(blank=True, verbose_name='Notes')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'scheduler_team',
                'ordering': ['-name', '-skill'],
            },
        ),
        migrations.CreateModel(
            name='Proposition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('start_time', models.TimeField(verbose_name='Start time')),
                ('end_time', models.TimeField(verbose_name='End time')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'scheduler_proposition',
                'ordering': ['-start_time', '-end_time'],
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('score_opponent', models.PositiveIntegerField(default=None, null=True, verbose_name='Score of the opponent')),
                ('score', models.PositiveIntegerField(default=None, null=True, verbose_name='Our score')),
                ('default_match_date', models.DateTimeField(verbose_name='Default match date')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('opponent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Team', verbose_name='Opponent')),
            ],
            options={
                'db_table': 'scheduler_match',
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_date', models.DateTimeField(default=None, null=True, verbose_name='Match date')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Match', unique=True, verbose_name='Match')),
            ],
            options={
                'db_table': 'scheduler_appointment',
                'ordering': ['-match_date', '-match__default_match_date'],
            },
        ),
    ]