# Generated by Django 3.2.7 on 2021-09-22 09:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('noteapp', '0011_alter_keepnotes_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keepnotes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
