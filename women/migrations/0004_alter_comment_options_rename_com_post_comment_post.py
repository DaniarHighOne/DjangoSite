# Generated by Django 4.0.5 on 2022-06-18 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0003_alter_comment_com_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date'], 'verbose_name': 'Коментарий', 'verbose_name_plural': 'Коментарии'},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='com_post',
            new_name='post',
        ),
    ]
