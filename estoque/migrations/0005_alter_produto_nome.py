# Generated by Django 4.0.5 on 2022-09-26 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0004_produto_slug_alter_produto_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='nome',
            field=models.CharField(max_length=40),
        ),
    ]