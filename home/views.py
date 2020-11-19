from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Category,SubCategory,Product,Customer
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.views import View

class Index(View):
    def post(self, request):
        product=request.POST.get('product')
        remove=request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' ,request.session['cart'])
        return redirect('index_all')

    def get(self,request,parent_or_child=None,pk=None):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
            
        categories=Category.objects.filter(parent=None)

        if parent_or_child is None:
            products = Product.objects.all()
        elif parent_or_child == 'child':
            sub_cat = SubCategory.objects.get(pk=pk)
            products = sub_cat.product_set.all()

        elif parent_or_child == 'parent':
            products = []
            sub_cats = Category.objects.get(pk=pk).children.all()

            for sub_cat in sub_cats:
                prds = sub_cat.product_set.all()
                products += prds

        else:
            products=[]
        print('you are : ',request.session.get('email'))
        return render(
            request,
            'products/index.html',
            {'categories':categories,'products':products}
            )


class Register(View):
    def get(self,request):
        return render(request, 'products/register.html')

    def post(self,request):
        postData = request.POST
        name = postData.get('name')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        # validation
        value = {'name': name, 'phone': phone, 'email': email}
        customer = Customer(name=name, phone=phone, email=email, password=password)
        err_msg = self.validateCustomer(customer)

        # saving
        if not err_msg:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('login')
        else:
            data = {'error': err_msg, 'values': value}
            return render(request, "products/register.html", data)

    def validateCustomer(self,customer):
        err_msg = None
        if (not customer.name):
            err_msg = "Name Required!"
        elif (not customer.phone):
            err_msg = "Phone No. required"
        elif not customer.validatePhone():
            err_msg = "Enter valid Phone no."
        elif len(customer.phone) < 10:
            err_msg = "Phone No. must have 10 digits"
        elif not customer.validateEmail():
            err_msg = 'Enter valid email'
        elif not customer.password:
            err_msg = "please create a password"
        elif len(customer.password) < 6:
            err_msg = "Password must be 6 char long"
        elif customer.doExists():
            err_msg = 'Email Address Already registered..'
        return err_msg


class Login(View):
    def get(self,request):
        return render(request, 'products/login.html')

    def post(self,request):

        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.get_customer_by_email(email)
        err_msg=None
        if customer:
            flag = check_password(password,customer.password)
            if flag:
                request.session['customer_id'] = customer.id
                request.session['customer_email'] = customer.email
                return render(request,'products/index.html')
            else:
                err_msg='Email or Password invalid'
        else:
            err_msg='Email or Password invalid'
        return render(request,'products/login.html',{'error':err_msg})


