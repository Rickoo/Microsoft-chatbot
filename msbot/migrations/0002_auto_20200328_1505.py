# Generated by Django 2.2.4 on 2020-03-28 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msbot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memory',
            name='sender',
        ),
        migrations.DeleteModel(
            name='Conversation',
        ),
        migrations.DeleteModel(
            name='Memory',
        ),
        migrations.DeleteModel(
            name='Sender',
        ),
    ]
