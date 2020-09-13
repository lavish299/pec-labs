# Generated by Django 3.1.1 on 2020-09-13 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200913_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='secondary_img',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.secondary_image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='secondary_image',
            name='equipment_id',
            field=models.IntegerField(),
        ),
    ]