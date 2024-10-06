# Generated by Django 4.2.16 on 2024-10-06 00:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('budgets', '0003_income'),
    ]

    operations = [
        migrations.RenameField(
            model_name='income',
            old_name='income',
            new_name='amount',
        ),
        migrations.AddField(
            model_name='income',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
