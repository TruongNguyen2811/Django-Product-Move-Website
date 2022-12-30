from django.urls import path
from . import views

urlpatterns = [
    path('', views.factoryProduct, name='factorymain'),
    path('createproduct/<str:pk>/',views.CreateProduct,name='CreateProducts'),
    path('createproduce/<str:pk>/', views.createProduce, name="createProduce"),
    path('UpdateStatus/<str:pkF>/<str:pkP>/',views.UpDateStatus, name='updateStatus'),
    path('createreceive/<str:pkF>/<str:pkP>/',views.CreateReceive,name='CreateReceive'),
    path('factoryWarranty/<str:pk>/',views.factoryWarrantyProduct,name='factoryWarranty'),
    path('factoryRecall/<str:pk>/',views.factoryReCallProduct,name='factoryReCallProduct'),
    path('UpdateStatusdone/<str:pkF>/<str:pkP>/',views.UpDateStatusDone, name='updateStatusDone'),
    path('Updatewarranty/<str:pkF>/<str:pkP>/',views.UpDateWarranty, name='UpDateWarranty'),
    path('DeleteProduct/<str:pkF>/<str:pkP>/',views.DeleteProduct,name='DeleteProduct')
    # path('base',views.GetAllFactory)
    
]