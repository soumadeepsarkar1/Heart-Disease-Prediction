# Generated by Django 3.2.4 on 2021-06-21 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testresult',
            name='modelChoice',
            field=models.CharField(default='model', max_length=30),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='name',
            field=models.CharField(default='name', max_length=100),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='result',
            field=models.CharField(max_length=30),
        ),
    ]
