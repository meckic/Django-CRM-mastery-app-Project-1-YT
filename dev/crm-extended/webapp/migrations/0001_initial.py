# Generated by Django 4.2 on 2024-09-04 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=255)),
                ('province', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=125)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=255)),
                ('province', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=125)),
                ('upload', models.ImageField(blank=True, upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('description', models.TextField(blank=True)),
                ('webpage', models.URLField()),
                ('attendees', models.ManyToManyField(blank=True, to='webapp.person')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.venue')),
            ],
        ),
    ]
