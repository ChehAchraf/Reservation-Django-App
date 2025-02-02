# Generated by Django 5.1.4 on 2024-12-27 12:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_highlight_remove_activities_highlights_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='activities_images/')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.activities')),
            ],
        ),
    ]
