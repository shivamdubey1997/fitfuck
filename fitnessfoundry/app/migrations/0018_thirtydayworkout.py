# Generated by Django 4.0.3 on 2023-05-30 19:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0017_alter_uploadworkoutvideo_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thirtydayworkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='thirtydayvideo')),
                ('tdwvideotitle', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('videodescriptionfortdw', models.TextField()),
                ('day', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('pinthdworkout', models.ManyToManyField(blank=True, related_name='likedthirty', to=settings.AUTH_USER_MODEL)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]