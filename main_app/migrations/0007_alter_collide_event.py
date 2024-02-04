# Generated by Django 5.0.1 on 2024-02-04 17:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_remove_collide_rsvps_remove_event_collides_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collide',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collides', to='main_app.event'),
        ),
    ]