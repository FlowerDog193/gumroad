# Generated by Django 3.2.12 on 2022-03-11 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_userlibrary_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='stripe_account_id',
            field=models.CharField(default='123', max_length=100),
            preserve_default=False,
        ),
    ]