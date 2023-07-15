# Generated by Django 4.2.2 on 2023-07-15 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ormRelations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('students', models.ManyToManyField(to='ormRelations.student')),
            ],
        ),
    ]
