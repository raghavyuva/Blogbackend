# Generated by Django 4.0.3 on 2022-03-22 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_blog_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='user', max_length=15, unique=True),
        ),
    ]
