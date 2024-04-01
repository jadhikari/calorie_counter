# Generated by Django 5.0.3 on 2024-03-31 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('carbs', models.FloatField()),
                ('protrin', models.FloatField()),
                ('fats', models.FloatField()),
                ('calories', models.IntegerField()),
            ],
        ),
    ]
