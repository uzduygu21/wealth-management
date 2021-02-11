# Generated by Django 3.1 on 2020-12-17 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0006_auto_20201216_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountnum', models.CharField(max_length=64)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('bank', models.CharField(max_length=64)),
                ('linkdate', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accountowner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]