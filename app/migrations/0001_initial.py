# Generated by Django 5.0.7 on 2024-07-29 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stu',
            fields=[
                ('sroll', models.IntegerField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=50)),
            ],
        ),
    ]
