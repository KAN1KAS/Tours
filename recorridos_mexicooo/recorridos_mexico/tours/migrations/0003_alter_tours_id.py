# Generated by Django 5.0.6 on 2024-07-12 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_alter_tours_ganancias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tours',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
