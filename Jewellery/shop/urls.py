from django.urls import path
from .import views


urlpatterns=[
path('',views.index,name='index'),    
    
path('Staff_Reg/',views.Sreg,name='Staff_Reg'),
path('stafflogin/',views.stafflog,name='SLOG'),
path('Slog/',views.Slog,name='slog'),
path('StaffDash/',views.StaffDash,name='StaffDash'),
path('AddProd/',views.AddProd,name='AddProd'),
path('UpProd/<str:pk>',views.UpProd,name='UpProd'),






path('registration/',views.registration,name='registration'),
path('custlog/',views.custlog,name='custlog'),
path('customer/',views.customer,name='customer'),
path('cart/',views.cart,name='cart'),
path('shop/',views.shop,name='shop'),
path('add/<str:pk>',views.add,name='add'),


path('data/',views.view,name='data'),

path('about/',views.about,name='about'),
path('contact-us/',views.contact,name='contact'),
path('welcome/',views.welcome,name='welcome'),
]