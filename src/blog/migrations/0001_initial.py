# Generated by Django 2.2.2 on 2020-03-21 11:09

import blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250)),
                ('body', models.TextField(blank=True, max_length=5000)),
                ('image', models.ImageField(blank=True, default='ww.png', upload_to=blog.models.upload_location)),
                ('date_published', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, max_length=250, unique=True)),
                ('photo_1', models.ImageField(blank=True, upload_to=blog.models.upload_location, verbose_name='Photo 1 (Optional)')),
                ('photo_2', models.ImageField(blank=True, upload_to=blog.models.upload_location, verbose_name='Photo 2 (Optional)')),
                ('photo_3', models.ImageField(blank=True, upload_to=blog.models.upload_location, verbose_name='Photo 3 (Optional)')),
                ('photo_4', models.ImageField(blank=True, upload_to=blog.models.upload_location, verbose_name='Photo 4 (Optional)')),
                ('photo_5', models.ImageField(blank=True, upload_to=blog.models.upload_location, verbose_name='Photo 5 (Optional)')),
                ('photo_6', models.ImageField(blank=True, upload_to=blog.models.upload_location, verbose_name='Photo 6 (Optional)')),
                ('photo_7', models.ImageField(blank=True, upload_to=blog.models.upload_location, verbose_name='Photo 7 (Optional)')),
                ('photo_8', models.ImageField(blank=True, upload_to=blog.models.upload_location, verbose_name='Photo 8 (Optional)')),
                ('photo_9', models.ImageField(blank=True, upload_to=blog.models.upload_location, verbose_name='Photo 9 (Optional)')),
                ('photo_10', models.ImageField(blank=True, upload_to=blog.models.upload_location, verbose_name='Photo 10 (Optional)')),
                ('photo_11', models.ImageField(blank=True, upload_to=blog.models.upload_location, verbose_name='Photo 11 (Optional)')),
                ('photo_12', models.ImageField(blank=True, upload_to=blog.models.upload_location, verbose_name='Photo 12 (Optional)')),
                ('photo_13', models.ImageField(blank=True, upload_to=blog.models.upload_location, verbose_name='Photo 13 (Optional)')),
                ('photo_14', models.ImageField(blank=True, upload_to=blog.models.upload_location, verbose_name='Photo 14 (Optional)')),
                ('photo_15', models.ImageField(blank=True, upload_to=blog.models.upload_location, verbose_name='Photo 15 (Optional)')),
                ('photo_16', models.ImageField(blank=True, upload_to=blog.models.upload_location, verbose_name='Photo 16 (Optional)')),
                ('photo_17', models.ImageField(blank=True, upload_to=blog.models.upload_location, verbose_name='Photo 17 (Optional)')),
                ('photo_18', models.ImageField(blank=True, upload_to=blog.models.upload_location, verbose_name='Photo 18 (Optional)')),
                ('photo_19', models.ImageField(blank=True, upload_to=blog.models.upload_location, verbose_name='Photo 19 (Optional)')),
                ('photo_20', models.ImageField(blank=True, upload_to=blog.models.upload_location, verbose_name='Photo 20 (Optional)')),
                ('photo_21', models.ImageField(blank=True, upload_to=blog.models.upload_location, verbose_name='Photo 21 (Optional)')),
                ('photo_22', models.ImageField(blank=True, upload_to=blog.models.upload_location, verbose_name='Photo 22 (Optional)')),
                ('photo_23', models.ImageField(blank=True, upload_to=blog.models.upload_location, verbose_name='Photo 23 (Optional)')),
                ('photo_24', models.ImageField(blank=True, upload_to=blog.models.upload_location, verbose_name='Photo 24 (Optional)')),
                ('photo_25', models.ImageField(blank=True, upload_to=blog.models.upload_location, verbose_name='Photo 25 (Optional)')),
                ('photo_26', models.ImageField(blank=True, upload_to=blog.models.upload_location, verbose_name='Photo 26 (Optional)')),
                ('photo_27', models.ImageField(blank=True, upload_to=blog.models.upload_location, verbose_name='Photo 27 (Optional)')),
                ('photo_28', models.ImageField(blank=True, upload_to=blog.models.upload_location, verbose_name='Photo 28 (Optional)')),
                ('photo_29', models.ImageField(blank=True, upload_to=blog.models.upload_location, verbose_name='Photo 29 (Optional)')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
