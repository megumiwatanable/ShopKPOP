# Generated by Django 4.0.5 on 2023-06-28 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_alter_khachhang_diachi_alter_khachhang_sodienthoai'),
        ('cart', '0003_remove_giohang_sanphamgiohang_giohang_giaban_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giohang',
            name='KhachHang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.khachhang'),
        ),
    ]
