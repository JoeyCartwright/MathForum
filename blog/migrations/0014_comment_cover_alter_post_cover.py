# Generated by Django 4.0.8 on 2022-12-03 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_post_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='cover',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]