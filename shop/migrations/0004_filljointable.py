# Generated by Django 2.2.5 on 2019-10-19 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20191019_1727'),
    ]

    operations = [
        migrations.RunSQL(
            "INSERT INTO shop_category_products VALUES (1,1,1);"),
        migrations.RunSQL(
            "INSERT INTO shop_category_products VALUES (2,3,3);"),
        migrations.RunSQL(
            "INSERT INTO shop_category_products VALUES (3,4,4);"),
        migrations.RunSQL(
            "INSERT INTO shop_category_products VALUES (4,5,5);"),
        migrations.RunSQL(
            "INSERT INTO shop_category_products VALUES (5,4,6);"),
        migrations.RunSQL(
            "INSERT INTO shop_category_products VALUES (6,4,7);"),
        migrations.RunSQL(
            "INSERT INTO shop_category_products VALUES (7,4,8);"),
        migrations.RunSQL(
            "INSERT INTO shop_category_products VALUES (8,6,9);"),
        migrations.RunSQL(
            "INSERT INTO shop_category_products VALUES (9,6,10);"),
        migrations.RunSQL(
            "INSERT INTO shop_category_products VALUES (10,2,2);")
    ]
