# Generated by Django 4.2.3 on 2023-07-30 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation_Room', '0002_alter_room_image1_alter_room_image2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='image1',
            field=models.FileField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='room',
            name='image2',
            field=models.FileField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='room',
            name='image3',
            field=models.FileField(upload_to='images/'),
        ),
    ]