# Generated by Django 3.0.7 on 2020-09-24 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_sectionpage_page_width'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmediasettings',
            name='twitter',
            field=models.CharField(blank=True, help_text='Your Twitter username (without the @ symbol, for example "NHSX")', max_length=255, null=True),
        ),
    ]
