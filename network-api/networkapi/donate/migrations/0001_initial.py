# Generated by Django 3.2.16 on 2023-03-30 19:06

import django.db.models.deletion
import wagtail.fields
import wagtailmetadata.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailimages", "0024_index_image_file_hash"),
        ("wagtailcore", "0078_referenceindex"),
    ]

    operations = [
        migrations.CreateModel(
            name="DonateLandingPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("intro", wagtail.fields.RichTextField()),
                (
                    "featured_image",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, related_name="+", to="wagtailimages.image"
                    ),
                ),
                (
                    "search_image",
                    models.ForeignKey(
                        blank=True,
                        help_text="Image must be high quality, include our logo mark and have the dimensions 1200 x 628 px. For more design guidelines see here: https://foundation.mozilla.org/en/docs/brand/brand-identity/social-media/#og-images",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                        verbose_name="Search image",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(wagtailmetadata.models.WagtailImageMetadataMixin, "wagtailcore.page", models.Model),
        ),
    ]
