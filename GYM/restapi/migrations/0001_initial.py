# Generated by Django 2.1.7 on 2020-02-07 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='memberShipPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trainerName', models.CharField(max_length=60)),
                ('classesName', models.CharField(max_length=60)),
                ('price', models.IntegerField()),
                ('time', models.IntegerField()),
            ],
        ),
    ]
