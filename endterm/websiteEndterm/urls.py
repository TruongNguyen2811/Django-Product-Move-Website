from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginPage,name='loginPage'),
    path('logoutUser/',views.logoutUser,name='logoutUser'),
    path('AdminDashBoard/',views.AdminDashBoard,name='AdminDashBoard'),
    path('registerAdmin/',views.registerAdmin,name='registerAdmin'),
    path('registerFactory/',views.registerFactory,name='registerFactory'),
    path('registerStore/',views.registerStore,name='registerStore'),
    path('registerWarrantyCenter/',views.registerWarrantyCenter,name='registerWarrantyCenter'),
    path('FactoryForms/',views.FactoryForms,name='FactoryForms'),
    path('StoreForms/',views.StoreForms,name='StoreForms'),
    path('WarrantyCenterForms/',views.WarrantyCenterForms,name='WarrantyCenterForms'),
    path('AdminForms/',views.AdminForms,name='AdminForms'),
    path('AllFactory/',views.AllFactory,name='AllFactory'),
    path('AllStores/',views.AllStores,name='AllStores'),
    path('AllWarrantyCenter/',views.AllWarrantyCenter,name='AllWarrantyCenter'),
    path('AllProduct/',views.AllProduct,name='AllProduct'),
    # path('index', views.index, name='index'),
    # path('base',views.GetAllFactory)
    
]