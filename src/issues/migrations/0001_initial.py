# Generated by Django 4.2 on 2023-04-14 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formerSubject', models.CharField(blank=True, max_length=60, null=True)),
                ('formerContent', models.TextField(blank=True, max_length=280, null=True)),
                ('formerType', models.CharField(blank=True, choices=[('B', 'Bug'), ('Q', 'Question'), ('E', 'Enhancement')], max_length=2, null=True)),
                ('formerSeverity', models.CharField(blank=True, choices=[('W', 'Whishlist'), ('M', 'Minor'), ('N', 'Normal'), ('I', 'Important'), ('C', 'Critical')], max_length=2, null=True)),
                ('formerPriority', models.CharField(blank=True, choices=[('L', 'Low'), ('N', 'Normal'), ('H', 'High')], max_length=2, null=True)),
                ('latterSubject', models.CharField(blank=True, max_length=60, null=True)),
                ('latterContent', models.TextField(blank=True, max_length=280, null=True)),
                ('latterType', models.CharField(blank=True, choices=[('B', 'Bug'), ('Q', 'Question'), ('E', 'Enhancement')], max_length=2, null=True)),
                ('latterSeverity', models.CharField(blank=True, choices=[('W', 'Whishlist'), ('M', 'Minor'), ('N', 'Normal'), ('I', 'Important'), ('C', 'Critical')], max_length=2, null=True)),
                ('latterPriority', models.CharField(blank=True, choices=[('L', 'Low'), ('N', 'Normal'), ('H', 'High')], max_length=2, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('content', models.TextField(max_length=280)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=60)),
                ('content', models.TextField(max_length=280)),
                ('type', models.CharField(choices=[('B', 'Bug'), ('Q', 'Question'), ('E', 'Enhancement')], default='B', max_length=2)),
                ('severity', models.CharField(choices=[('W', 'Whishlist'), ('M', 'Minor'), ('N', 'Normal'), ('I', 'Important'), ('C', 'Critical')], default='N', max_length=2)),
                ('priority', models.CharField(choices=[('L', 'Low'), ('N', 'Normal'), ('H', 'High')], default='N', max_length=2)),
                ('blocked', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Issue',
                'verbose_name_plural': 'Issues',
            },
        ),
    ]
