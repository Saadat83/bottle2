# Generated by Django 4.1 on 2022-08-24 09:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('post_date', models.DateField(default=django.utils.timezone.now)),
                ('image', models.ImageField(default='default.jpg', upload_to='post_image/')),
            ],
        ),
    ]
