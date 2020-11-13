from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Category,SubCategory,Product

def index_view(request,parent_or_child=None,pk=None):
    categories=Category.objects.filter(parent=None)

    if parent_or_child is None:
        products=Product.objects.all()
    elif parent_or_child=='child':
        sub_cat=SubCategory.objects.get(pk=pk)
        products=sub_cat.product_set.all()

    elif parent_or_child=='parent':
        products=[]
        sub_cats=Category.objects.get(pk=pk).children.all()

        for sub_cat in sub_cats:
            prds=sub_cat.product_set.all()
            products +=prds

    else:
        products=[]

    return  render(
        request,
        'products/index.html',
        {'categories':categories,'products':products}
    )


def login(request):
    return render(request , 'products/login.html')   