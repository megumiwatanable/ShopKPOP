# Generated by Django 4.0.5 on 2023-06-28 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0007_alter_chuyenmuc_options_alter_mausac_options_and_more'),
        ('customer', '0004_alter_khachhang_diachi_alter_khachhang_sodienthoai'),
    ]

    operations = [
        migrations.CreateModel(
            name='SanPhamGioHang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TenSanPham', models.CharField(max_length=255)),
                ('MoTaNgan', models.TextField(max_length=255)),
                ('GiaBan', models.IntegerField()),
                ('SoLuong', models.ImageField(default=1, upload_to='')),
                ('KhachHang', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customer.khachhang')),
                ('MauSac', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.mausac')),
                ('SanPham', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.sanpham')),
            ],
            options={
                'verbose_name': 'Sản Phẩm Giỏ Hàng',
                'verbose_name_plural': 'Sản Phẩm Giỏ Hàng',
            },
        ),
        migrations.CreateModel(
            name='GioHang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('KhachHang', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customer.khachhang')),
                ('SanPhamGioHang', models.ManyToManyField(to='cart.sanphamgiohang')),
            ],
            options={
                'verbose_name': 'Giỏ Hàng',
                'verbose_name_plural': 'Giỏ Hàng',
            },
        ),
    ]
