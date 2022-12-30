from django.urls import path
from . import views

urlpatterns = [
    path('', views.StoreDashBoard, name='storeDashboard'),
    path('newclientform/<str:pk>/',views.AddNewClient,name='AddNewClient'),
    path('neworderform/<str:pk>/',views.AddNewOrder,name='AddNewOrder'),
    path('productsold/<str:pk>/',views.StoreSoldBoard,name='StoreSoldBoard'),
    path('clientview/<str:pkS>/<str:pkC>/',views.ClientsDetails, name='ClientDetails'),
    path('recall/<str:pkS>/<str:pkP>/',views.recall, name='recall'),
    path('recallToWarranty/<str:pkS>/<str:pkP>/',views.recallToWarranty, name='recallToWarranty'),
    path('SoldStatus/<str:pkS>/<str:pkP>/',views.SoldStatus, name='SoldStatus'),
    # path('createproduce/<str:pk>/', views.createProduce, name="createProduce")
    # path('base',views.GetAllFactory)
    
]