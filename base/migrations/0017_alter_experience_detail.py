# Generated by Django 4.1.3 on 2024-02-11 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0016_alter_experience_detail"),
    ]

    operations = [
        migrations.AlterField(
            model_name="experience",
            name="detail",
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
