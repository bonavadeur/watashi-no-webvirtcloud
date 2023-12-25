# Generated by Django 3.2.15 on 2022-08-23 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interfaces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'required': 'No interface name has been entered'}, max_length=20, verbose_name='name')),
                ('type', models.CharField(max_length=12, verbose_name='status')),
                ('state', models.CharField(max_length=100, verbose_name='device')),
                ('mac', models.CharField(max_length=24, verbose_name='forward')),
            ],
            options={
                'managed': False,
            },
        ),
    ]