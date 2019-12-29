# Generated by Django 2.2.7 on 2019-12-20 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('blog_id', models.AutoField(primary_key=True, serialize=False)),
                ('blog_name', models.CharField(max_length=200)),
                ('cat_id', models.IntegerField(choices=[(6, 'Thời sự'), (7, 'Giới trẻ'), (8, 'Sức khỏe'), (9, 'Thế giới'), (10, 'Văn hóa'), (11, 'Đời sống')])),
                ('blog_img', models.ImageField(max_length=255, upload_to='')),
                ('description', models.TextField()),
                ('date_create', models.DateField()),
            ],
            options={
                'db_table': 'tbl_blog',
            },
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_img',
            field=models.ImageField(max_length=255, upload_to=''),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'Hien thi'), (0, 'An'), (2, 'An1')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='cat_id',
            field=models.IntegerField(choices=[(6, 'Thời sự'), (7, 'Giới trẻ'), (8, 'Sức khỏe'), (9, 'Thế giới'), (10, 'Văn hóa'), (11, 'Đời sống')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='pro_img',
            field=models.ImageField(max_length=255, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='pro_name',
            field=models.CharField(max_length=200),
        ),
    ]
