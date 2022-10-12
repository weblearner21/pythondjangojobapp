# Generated by Django 4.1.2 on 2022-10-12 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_skills_jobapp_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapp',
            name='type',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], default='Full Time', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobapp',
            name='description',
            field=models.TextField(),
        ),
    ]
