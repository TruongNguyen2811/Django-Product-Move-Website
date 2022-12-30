from django.urls import path
from . import views

urlpatterns = [
    path('', views.WarrantyDashBoard, name='WarrantyDashboard'),
    path('MoveBackProduct/<str:pk>/', views.MoveBackProduct, name='MoveBackProduct'),
    path('AllWarrantyProduct/<str:pk>/', views.AllWarrantyProduct, name='AllWarrantyProduct'),
    path('clientview/<str:pkW>/<str:pkC>/',views.ClientsDetail,name='ClientsDetail'),
    path('updatestatus/<str:pkW>/<str:pkP>/',views.UpDateStatus,name='UpdateStatusWarranty'),
    path('CreateWarranty/<str:pkW>/<str:pkP>/',views.UpDateWarranty,name='UpdateWarranty'),
    path('updatesWarrantedProduct/<str:pkW>/<str:pkP>/',views.UpdateDoneProduct,name='UpdateDoneInProduct'),
    path('updatesWarrantedWarranty/<str:pkW>/<str:pkP>/',views.UpDateWarrantyinWarranty,name='UpdateDoneInWarranty'),
    
]