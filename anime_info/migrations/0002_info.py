# Generated by Django 4.2.3 on 2023-07-11 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('language', models.CharField(max_length=20)),
                ('release_year', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
