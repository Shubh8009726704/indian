# Generated by Django 4.1.10 on 2023-08-18 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ADIT', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='address',
            new_name='pro_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='photo',
            new_name='pro_photo',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='name',
            new_name='pro_price',
        ),
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.AddField(
            model_name='student',
            name='pro_desc',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
