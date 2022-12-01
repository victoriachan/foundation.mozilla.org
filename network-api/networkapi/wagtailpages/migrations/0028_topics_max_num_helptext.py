# Generated by Django 3.2.13 on 2022-06-03 22:53

import modelcluster.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "wagtailpages",
            "0027_rename_blogpagecategory_blogpagetopic_rename_categoryfilter_topicfilter",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpage",
            name="topics",
            field=modelcluster.fields.ParentalManyToManyField(
                blank=True,
                help_text="Which blog topics is this blog page associated with? Please select 2 topics max.",
                to="wagtailpages.BlogPageTopic",
                verbose_name="Topics",
            ),
        ),
    ]
