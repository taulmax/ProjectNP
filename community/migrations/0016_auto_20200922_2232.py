# Generated by Django 3.1.1 on 2020-09-22 13:32

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0015_auto_20200921_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='내용'),
        ),
    ]
