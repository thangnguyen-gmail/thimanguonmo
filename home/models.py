from django.db import models

# Create your models here.
statusChoice = ((1,'Hien thi'),(0,'An'), (2,'An1'))
class Category(models.Model) : 
    cat_id = models.AutoField(primary_key = 'true')
    cat_name = models.CharField(max_length = 50, null = False)
    cat_img = models.ImageField(max_length = 255)
    status = models.SmallIntegerField(choices=statusChoice)
    date_create = models.DateField()
    class Meta : 
        db_table = "tbl_Category"
class Product(models.Model) : 
    listCategory  = Category.objects.all()
    result = []
    for item in  listCategory : 
        result .append(
            (item.cat_id, item.cat_name)
        )
    pro_id = models.AutoField(primary_key ='true')
    pro_name = models.CharField(max_length = 200,null = False)
    cat_id = models.IntegerField(null= False, choices=result)
    pro_img = models.ImageField(max_length = 255)
    description = models.TextField()
    date_create = models.DateField()
    class Meta :
        db_table = "tbl_product"
class blog(models.Model) : 
    listCategory  = Category.objects.all()
    result = []
    for item in  listCategory : 
        result .append(
            (item.cat_id, item.cat_name)
        )
    blog_id = models.AutoField(primary_key ='true')
    blog_name = models.CharField(max_length = 200,null = False)
    cat_id = models.IntegerField(null= False, choices=result)
    blog_img = models.ImageField(max_length = 255)
    description = models.TextField()
    date_create = models.DateField()
    class Meta :
        db_table = "tbl_blog"