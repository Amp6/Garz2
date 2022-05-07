# Generated by Django 4.0.4 on 2022-05-04 19:00

from django.db import migrations, models
import djongo.models.fields
import garbanzos.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('path', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='upload')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('hash', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('category', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('price', models.FloatField()),
                ('preview', models.FileField(upload_to='')),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('shadow', models.CharField(max_length=20)),
                ('birthdate', models.DateField()),
                ('bills', djongo.models.fields.ArrayField(model_container=garbanzos.models.Bill)),
                ('address', djongo.models.fields.ArrayField(model_container=garbanzos.models.Address)),
            ],
        ),
    ]
