# Generated by Django 2.0.8 on 2018-08-16 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sysv', '0003_auto_20180816_0347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='imagem',
            field=models.ImageField(upload_to='produtos/'),
        ),
    ]
