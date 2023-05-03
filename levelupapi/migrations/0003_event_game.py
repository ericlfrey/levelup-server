# Generated by Django 4.2 on 2023-05-03 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0002_rename_type_game_game_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='game',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='organized_events', to='levelupapi.game'),
        ),
    ]
