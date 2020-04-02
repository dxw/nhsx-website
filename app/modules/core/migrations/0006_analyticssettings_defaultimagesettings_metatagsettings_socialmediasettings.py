# Generated by Django 3.0.4 on 2020-04-02 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('core', '0005_auto_20200402_1115'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(blank=True, help_text='Your Facebook page URL', null=True)),
                ('instagram', models.CharField(blank=True, help_text='Your Instagram url', max_length=255, null=True)),
                ('twitter', models.CharField(blank=True, help_text='Your Twitter url', max_length=255, null=True)),
                ('youtube', models.CharField(blank=True, help_text='Your YouTube url', max_length=255, null=True)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'Social media accounts',
            },
        ),
        migrations.CreateModel(
            name='MetaTagSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, help_text='The short description shown in search results (160 characters max)', null=True)),
                ('image', models.ForeignKey(blank=True, help_text='A default image to use when shared on Facebook (aim for 1200x630)', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.NHSXImage')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'Meta and social sharing tags',
            },
        ),
        migrations.CreateModel(
            name='DefaultImageSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ForeignKey(blank=True, help_text='A default image to use when none is present for a page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.NHSXImage')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'Default / fallback image settings',
            },
        ),
        migrations.CreateModel(
            name='AnalyticsSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_id', models.CharField(blank=True, help_text='Property ID', max_length=32, null=True)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'Analytics settings',
            },
        ),
    ]