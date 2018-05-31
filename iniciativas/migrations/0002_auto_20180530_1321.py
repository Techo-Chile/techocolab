# Generated by Django 2.0.1 on 2018-05-30 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iniciativas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Community_issue_attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='0000000', editable=False, max_length=200)),
                ('value_type', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='community_issue',
            old_name='comm_issue_description',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='community_issue',
            name='comm_issue_name',
        ),
        migrations.RemoveField(
            model_name='community_issue',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='community_issue',
            name='name',
            field=models.CharField(default='0000000', editable=False, max_length=100),
        ),
        migrations.AddField(
            model_name='community_issue_attribute',
            name='Community_issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iniciativas.Community_issue'),
        ),
    ]