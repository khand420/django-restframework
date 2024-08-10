# Generated by Django 5.0.7 on 2024-07-23 18:24

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('is_done', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TimingTodo',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('timing', models.DateTimeField()),
                ('todo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.todo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
