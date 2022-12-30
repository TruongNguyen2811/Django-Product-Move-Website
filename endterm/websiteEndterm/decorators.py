from django.http import HttpResponse
from django.shortcuts import redirect


def allowed_admin():
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            if group == 'admins':
                return view_func(request, *args,**kwargs)
            if group =='factorys':
                return redirect('/factory/')
            if group =='Stores':
                return redirect('/store/')
            if group =='warrantyCenters':
                return redirect('/warrantycenter/')
        return wrapper_func
    return decorator

def allowed_factory():
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            if group == 'factorys':
                return view_func(request, *args,**kwargs)
            if group =='admins':
                return redirect('/AdminDashBoard/')
            if group =='Stores':
                return redirect('/store/')
            if group =='warrantyCenters':
                return redirect('/warrantycenter/')
        return wrapper_func
    return decorator

def allowed_Store():
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            if group == 'Stores':
                return view_func(request, *args,**kwargs)
            if group =='factorys':
                return redirect('/factory/')
            if group =='admins':
                return redirect('/AdminDashBoard/')
            if group =='warrantyCenters':
                return redirect('/warrantycenter/')
        return wrapper_func
    return decorator

def allowed_WarrantyCenter():
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            if group == 'warrantyCenters':
                return view_func(request, *args,**kwargs)
            if group =='factorys':
                return redirect('/factory/')
            if group =='Stores':
                return redirect('/store/')
            if group =='admins':
                return redirect('/AdminDashBoard/')
        return wrapper_func
    return decorator


# def only_WarrantyCenter(view_func):
#     def wrapper_func(request, *args, **kwargs):
#         group = None
#         if request.user.groups.exists():
#             group=request.user.groups.all()[0].name
#         if group == 'warrantyCenters':
#             return view_func(request, *args, **kwargs)
#         if group =='admins':
#             return redirect('/AdminDashBoard/')
#         if group =='Stores':
#             return redirect('/store/')
#         if group =='factorys':
#             return redirect('/factory/')
#         return wrapper_func
    
         