# Generated by Django 2.2.16 on 2022-07-25 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20220725_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='posts/', verbose_name='Картинка'),
        ),
    ]