
from django.db import models
from .managers import CategoryManager,SubCategoryManager

class Node(models.Model):
    name=models.CharField(max_length=150)
    parent=models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
    class Meta:
        ordering=('name',)


class Category(Node):
    objects=CategoryManager()
    class Meta:
        proxy=True

class SubCategory(Node):
    objects=SubCategoryManager()
    class Meta:
        proxy=True






class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)

    sub_category = models.ForeignKey(
        SubCategory,on_delete=models.CASCADE,default='')
    description = models.CharField(max_length=200, default='',null=True , blank=True)
    image = models.ImageField(upload_to='uploads/products/',default='',null=True )


    def __str__(self):
        return self.name
