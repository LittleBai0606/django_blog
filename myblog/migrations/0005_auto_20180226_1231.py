# Generated by Django 2.0.2 on 2018-02-26 04:31

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0004_counts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=ckeditor.fields.RichTextField(default='', verbose_name='正文'),
        ),
    ]