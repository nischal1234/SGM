# Generated by Django 2.2.10 on 2021-07-12 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('middlename', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('permanent_address', models.CharField(max_length=12)),
                ('temporary_address', models.CharField(max_length=12)),
                ('dateofbirth', models.DateTimeField(null=True)),
                ('joindate', models.DateTimeField(null=True)),
                ('expyear', models.IntegerField(null=True)),
                ('pnumber', models.CharField(max_length=13)),
                ('snumber', models.CharField(max_length=13)),
                ('citizenship', models.CharField(max_length=15)),
                ('fathername', models.CharField(max_length=30)),
                ('grandfathername', models.CharField(max_length=30)),
                ('education', models.CharField(max_length=30)),
                ('assignpost', models.CharField(max_length=30)),
                ('pastcname', models.CharField(max_length=40)),
                ('pannumber', models.CharField(max_length=20)),
                ('height', models.CharField(max_length=5)),
                ('skincolor', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('maritual', models.CharField(max_length=10)),
                ('bloodgroup', models.CharField(max_length=5)),
            ],
        ),
    ]
