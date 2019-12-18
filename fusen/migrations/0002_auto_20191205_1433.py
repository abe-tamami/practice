# Generated by Django 3.0 on 2019-12-05 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fusen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fusen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('text', models.TextField(blank=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Memo',
        ),
    ]