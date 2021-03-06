# Generated by Django 3.1.1 on 2020-09-16 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-id'], 'verbose_name': '게시글', 'verbose_name_plural': '게시글'},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='context',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.AddField(
            model_name='post',
            name='hits',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='수정날짜'),
        ),
    ]
