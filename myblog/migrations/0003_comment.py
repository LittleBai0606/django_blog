# Generated by Django 2.0.2 on 2018-02-23 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_auto_20180222_2213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='无名大侠', max_length=20, verbose_name='姓名')),
                ('content', models.TextField(max_length=500, verbose_name='内容')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.Blog', verbose_name='所属博客')),
            ],
            options={
                'verbose_name': '博客评论',
                'verbose_name_plural': '博客评论',
            },
        ),
    ]
