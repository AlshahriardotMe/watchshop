from django.shortcuts import render
from django.views import View
from .models import Product , Customer, Cart, OrderPlaced
# Create your views here.

# *******product-detail*******

class ProductViews(View):
    def get(self, request):
        Analogwatch = Product.objects.filter(category = 'A')
        Smartwatch = Product.objects.filter(category = 'S')
        Wallclock = Product.objects.filter(category = 'W')
        Tableclock = Product.objects.filter(category = 'T')

        data = {
            'Analogwatch':Analogwatch,
            'Smartwatch':Smartwatch,
            'Wallclock':Wallclock,
            'Tableclock':Tableclock 
        }
        return render(request,'Shop/home.html', data)

# def product_detail(request):

#     return render(request,'Shop/product-detail.html')


class productdetail(View):
    def get(self, request, pk ):
        product = Product.objects.get(pk=pk)

        data={
            'product':product
        }
        return render(request,'Shop/product-detail.html',data)


# *******login**********
def Login(request):
    return render(request,'Shop/login.html') 


# *******Registration**********
def Registration(request):
    return render(request,'Shop/registration.html')

# *******Forgotpassword**********
def Forgotpassword(request):
    return render(request,'Shop/forgotpassword.html')

# *******Changepassword**********
def Changepassword(request):
    return render(request,'Shop/changepassword.html')

# *******service**********
def Service(request):
    return render(request,'Shop/service.html')

#*******Profile*********** 
def Profile(request):
    return render(request,'Shop/profile.html')

#*******Address*********** 
def Address(request):
    return render(request,'Shop/address.html')

#*******About*********** 
def About(request):
    return render(request,'Shop/about.html')

#*******Blog*********** 
def Blog(request):
    return render(request,'Shop/blog.html')

#*******Cart*********** 
def Cart(request):
    return render(request,'Shop/cart.html')

#*******Checkout*********** 
def Checkout(request):
    return render(request,'Shop/checkout.html')

    
#*******Tracking*********** 
def Tracking(request):
    return render(request,'Shop/tracking.html')


#*******Contact*********** 
def Contact(request):
    return render(request,'Shop/contact.html')