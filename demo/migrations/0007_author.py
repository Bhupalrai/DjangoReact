# Generated by Django 3.2.2 on 2021-05-13 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0006_alter_character_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('books', models.ManyToManyField(to='demo.Book')),
            ],
        ),
    ]
