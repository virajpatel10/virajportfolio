# Generated by Django 4.1.3 on 2024-01-22 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0003_alter_skill_body"),
    ]

    operations = [
        migrations.RemoveField(model_name="skill", name="body",),
        migrations.AddField(
            model_name="skill", name="per", field=models.IntegerField(default=50),
        ),
    ]
