# Generated by Django 4.1.4 on 2023-03-28 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Authentication", "0002_alter_user_phone_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="gender",
            field=models.CharField(
                blank=True, max_length=10, null=True, verbose_name="gender"
            ),
        ),
    ]
