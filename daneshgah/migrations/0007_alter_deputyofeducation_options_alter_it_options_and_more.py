# Generated by Django 4.2.6 on 2023-10-31 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("daneshgah", "0006_alter_it_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="deputyofeducation",
            options={
                "verbose_name": "Deputy of Education",
                "verbose_name_plural": "Deputy of Educations",
            },
        ),
        migrations.AlterModelOptions(
            name="it",
            options={"verbose_name": "IT", "verbose_name_plural": "ITs"},
        ),
        migrations.AlterModelOptions(
            name="professor",
            options={"verbose_name": "Professor", "verbose_name_plural": "Professors"},
        ),
        migrations.AlterModelOptions(
            name="student",
            options={"verbose_name": "Student", "verbose_name_plural": "Students"},
        ),
    ]
