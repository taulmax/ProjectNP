# Generated by Django 3.1.1 on 2020-09-20 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0009_post_recommend_count'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
