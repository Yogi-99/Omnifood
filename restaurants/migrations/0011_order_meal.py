# Generated by Django 2.2.4 on 2019-09-07 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0010_auto_20190906_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='meal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurants.Meal'),
        ),
    ]
