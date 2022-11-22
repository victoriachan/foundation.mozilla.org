# Generated by Django 3.1.11 on 2021-12-09 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("highlights", "0007_localize_migration"),
    ]

    operations = [
        migrations.AlterField(
            model_name="highlight",
            name="description",
            field=models.TextField(help_text="Description of the highlight", max_length=5000),
        ),
        migrations.AlterField(
            model_name="highlight",
            name="link_label",
            field=models.CharField(
                help_text="Text to show that links to this highlight's details page",
                max_length=300,
            ),
        ),
        migrations.AlterField(
            model_name="highlight",
            name="link_url",
            field=models.URLField(help_text="Link to this highlight's details page", max_length=2048),
        ),
        migrations.AlterField(
            model_name="highlight",
            name="title",
            field=models.CharField(help_text="Title of the highlight", max_length=300),
        ),
    ]
