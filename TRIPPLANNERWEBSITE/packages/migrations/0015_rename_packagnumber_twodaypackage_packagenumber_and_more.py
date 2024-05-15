# Generated by Django 4.2.6 on 2023-12-30 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0014_rename_packagnumber_threedaypackage_packagenumber_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='twodaypackage',
            old_name='packagnumber',
            new_name='packagenumber',
        ),
        migrations.RenameField(
            model_name='twodaypackage',
            old_name='spotnumber',
            new_name='spottime',
        ),
        migrations.AddField(
            model_name='twodaypackage',
            name='daynumber',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
