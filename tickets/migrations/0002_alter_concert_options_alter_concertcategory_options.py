# Generated by Django 4.2.4 on 2023-08-15 20:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tickets", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="concert",
            options={"ordering": ["starts_at"]},
        ),
        migrations.AlterModelOptions(
            name="concertcategory",
            options={
                "ordering": ["-name"],
                "verbose_name": "concert category",
                "verbose_name_plural": "concert categories",
            },
        ),
    ]