# Generated by Django 4.2.1 on 2023-05-12 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0004_auto_20230511_1009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Elected',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Тема')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('create_data', models.DateTimeField(auto_now_add=True)),
                ('update_data', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-create_data'],
            },
        ),
    ]
