# Generated by Django 4.0.5 on 2023-06-15 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_alter_thongtin_loaithongtin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thongtin',
            name='HinhAnh',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]