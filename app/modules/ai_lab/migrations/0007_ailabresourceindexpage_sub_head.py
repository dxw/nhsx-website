# Generated by Django 3.0.4 on 2020-07-15 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ai_lab", "0006_ailabexternalresource"),
    ]

    operations = [
        migrations.AddField(
            model_name="ailabresourceindexpage",
            name="sub_head",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
