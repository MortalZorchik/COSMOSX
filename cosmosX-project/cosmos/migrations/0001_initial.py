# Generated by Django 4.1.4 on 2023-01-02 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='cosmos/static/images')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
