# Generated by Django 4.1.5 on 2024-01-31 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0003_mark'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='name',
            field=models.ForeignKey(default='Null', on_delete=django.db.models.deletion.CASCADE, to='family.student'),
        ),
    ]
