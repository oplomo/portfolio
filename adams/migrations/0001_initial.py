# Generated by Django 5.2.3 on 2025-06-26 00:25

import adams.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to=adams.models.upload_to)),
                ('resume', models.FileField(blank=True, null=True, upload_to='resumes/')),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=adams.models.upload_to)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HeroSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=255)),
                ('subheading', models.TextField()),
                ('background_image', models.ImageField(blank=True, null=True, upload_to=adams.models.upload_to)),
                ('cta_text', models.CharField(blank=True, max_length=50, verbose_name='Call-to-action Text')),
                ('cta_link', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('tech_stack', models.CharField(help_text='Comma-separated technologies', max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to=adams.models.upload_to)),
                ('github_link', models.URLField(blank=True)),
                ('live_link', models.URLField(blank=True)),
                ('featured', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('icon_class', models.CharField(help_text="Font Awesome class, e.g., 'fa fa-code'", max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SiteMeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_title', models.CharField(max_length=100)),
                ('tagline', models.CharField(blank=True, max_length=255)),
                ('logo', models.ImageField(blank=True, null=True, upload_to=adams.models.upload_to)),
                ('favicon', models.ImageField(blank=True, null=True, upload_to=adams.models.upload_to)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('proficiency', models.IntegerField(help_text='Enter value from 0 to 100')),
                ('category', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('icon_class', models.CharField(help_text="e.g., 'fab fa-twitter'", max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(blank=True, max_length=100)),
                ('message', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to=adams.models.upload_to)),
            ],
        ),
    ]
