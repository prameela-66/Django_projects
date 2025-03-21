# Generated by Django 5.1.5 on 2025-03-03 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('std_app', '0002_student1_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
