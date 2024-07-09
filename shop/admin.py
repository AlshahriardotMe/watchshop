from django.contrib import admin

# Register your models here.
from .models import (
    Customer,
    Product,
    Cart,
    OrderPlaced

)

# customer model


@admin.register(Customer)  
class customerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name', 'phone','division','district','upazila','village','zipcode','image']

# product model

@admin.register(Product)
class productadmin(admin.ModelAdmin):
    list_display = ['id','title','selling_price','discounted_price','descrition', 'brand','category','product_image']


# cart model

@admin.register(Cart)
class cartadmin(admin.ModelAdmin):
    list_display= ['id','user','product','quantity']



# orderplace model

@admin.register(OrderPlaced)
class orderplacedadmin(admin.ModelAdmin):
    list_display = ['id','user','customer','product','quantity','ordered_date','status']
