# Generated by Django 2.0.1 on 2018-05-30 19:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('iniciativas', '0002_auto_20180530_1321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('image', models.ImageField(default='settings.MEDIA_ROOT/default.jpg', upload_to='images/%Y/%m/%d')),
                ('datestamp', models.DateTimeField(auto_now_add=True)),
                ('upload_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_documents', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='community_issue',
            name='name',
            field=models.CharField(default='0000000', max_length=100),
        ),
        migrations.AlterField(
            model_name='community_issue_attribute',
            name='Community_issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iniciativas.Community_issue'),
        ),
        migrations.AlterField(
            model_name='community_issue_attribute',
            name='name',
            field=models.CharField(default='0000000', max_length=200),
        ),
        migrations.AddField(
            model_name='community_issue',
            name='image',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='iniciativas.Image'),
        ),
    ]
