# Generated by Django 4.0.4 on 2022-07-27 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo', models.CharField(max_length=150)),
                ('status', models.IntegerField(choices=[(0, 'En Progreso'), (1, 'Finalizado')], default=(0, 'En Progreso'))),
            ],
        ),
    ]
