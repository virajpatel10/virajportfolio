# Generated by Django 4.1.3 on 2024-01-31 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0011_alter_education_gpa"),
    ]

    operations = [
        migrations.AlterField(
            model_name="education",
            name="gpa",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
