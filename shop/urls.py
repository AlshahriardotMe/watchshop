from django.urls import path
from shop import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.ProductViews.as_view(), name='home'),
    path('productdetail/<int:pk>', views.productdetail.as_view(), name='product_detail'),
    path('Login/', views.Login, name= 'login'),
    path('Registration/', views.Registration, name= 'Registration'),
    path('Forgotpassword/', views.Forgotpassword, name= 'Forgotpassword'),
    path('Changepassword/', views.Changepassword, name= 'Changepassword'),
    path('Service/', views.Service, name= 'Service'),

    path('Profile/', views.Profile, name= 'Profile'),
    path('Address/', views.Address, name= 'Address'),
    path('About/', views.About, name= 'About'),
    path('Blog/', views.Blog, name= 'Blog'),
    path('Cart/', views.Cart, name= 'Cart'),
    path('Checkout/', views.Checkout, name= 'Checkout'),
    path('Tracking/', views.Tracking, name= 'Tracking'),
    path('Contact/', views.Contact, name= 'Contact'),

    
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
