# Generated by Django 2.0.1 on 2018-05-30 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iniciativas', '0003_auto_20180530_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community_issue_attribute',
            name='Community_issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iniciativas.Community_issue'),
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(default='0000000', max_length=100),
        ),
    ]
