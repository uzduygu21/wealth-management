# Generated by Django 3.1 on 2020-12-16 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0005_auto_20201216_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='question',
            field=models.TextField(),
        ),
    ]
