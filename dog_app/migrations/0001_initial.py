# Generated by Django 4.2.3 on 2023-07-12 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=50)),
                ('friendliness', models.IntegerField()),
                ('trainability', models.IntegerField()),
                ('sheddingamount', models.IntegerField()),
                ('exerciseneeds', models.IntegerField()),
            ],
        ),
    ]
