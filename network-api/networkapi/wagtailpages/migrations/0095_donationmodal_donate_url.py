# Generated by Django 3.2.20 on 2023-08-03 20:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0094_alter_petition_campaign_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='donationmodal',
            name='donate_url',
            field=models.CharField(default='?form=donate', help_text='If you would like this modal to link to a custom URL, please enter a valid URL (starting with http:// or https://), or a valid query string starting with ? (Ex: ?form=donate).', max_length=255, validators=[django.core.validators.RegexValidator(message='Please enter a valid URL (starting with http:// or https://), or a valid query string starting with ? (Ex: ?form=donate).', regex='^(https?://[\\w.-]+(/\\S*)?)?(\\?[\\w-]+(=[\\w-]*)?(&[\\w-]+(=[\\w-]*)?)*)?$')]),
        ),
    ]
