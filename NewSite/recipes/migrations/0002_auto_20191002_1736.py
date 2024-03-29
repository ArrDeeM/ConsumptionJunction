# Generated by Django 2.2.5 on 2019-10-02 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='dateOfBirth',
            field=models.DateField(help_text='Enter date of birth', max_length=20),
        ),
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(help_text='Enter email', max_length=100),
        ),
    ]
