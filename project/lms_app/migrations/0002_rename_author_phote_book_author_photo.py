# Generated by Django 5.0.3 on 2024-06-27 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author_phote',
            new_name='author_photo',
        ),
    ]
