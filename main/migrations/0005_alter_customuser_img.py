# Generated by Django 5.1.1 on 2024-09-20 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_customuser_shopping_cart_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='img',
            field=models.ImageField(default='media/featured-02.png', upload_to='media/profile_images/', verbose_name='image'),
        ),
    ]
