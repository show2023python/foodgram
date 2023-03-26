# Generated by Django 3.0.3 on 2023-03-23 11:31

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
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(blank=True, null=True, upload_to='product_pictures/%Y/%m/%d')),
                ('store_name', models.CharField(max_length=1000)),
                ('kinds', models.CharField(blank=True, max_length=1000, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=8, null=True)),
                ('place_prefecture', models.CharField(blank=True, max_length=1000, null=True)),
                ('place_another', models.CharField(blank=True, max_length=1000, null=True)),
                ('comments', models.CharField(blank=True, max_length=1000, null=True)),
                ('main_comments', models.CharField(blank=True, max_length=1000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'products',
                'ordering': ['-created_at'],
            },
        ),
    ]