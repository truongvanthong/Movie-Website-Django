# Generated by Django 4.2 on 2023-04-25 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_alter_movie_budget_alter_movie_director_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="director",
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name="movie",
            name="director_img",
            field=models.CharField(max_length=2000, null=True),
        ),
    ]
