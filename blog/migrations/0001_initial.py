# Generated by Django 4.2.2 on 2023-08-09 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_text', models.TextField(verbose_name='Texto Principal')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='Data Publicação')),
            ],
        ),
    ]
