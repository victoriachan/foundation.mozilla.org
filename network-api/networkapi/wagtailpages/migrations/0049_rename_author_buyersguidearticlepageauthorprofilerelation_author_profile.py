# Generated by Django 3.2.13 on 2022-08-03 00:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0048_auto_20220803_0038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buyersguidearticlepageauthorprofilerelation',
            old_name='author',
            new_name='author_profile',
        ),
    ]
