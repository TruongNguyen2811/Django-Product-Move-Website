from django.contrib import admin
# from django.contrib.auth.models import User
from .models import factory, product,produce,store,receive,client,sell,warranty,warrantycenter
# Register your models here.


# admin.site.register(User)
admin.site.register(factory)
admin.site.register(produce)
admin.site.register(product)
admin.site.register(store)
admin.site.register(receive)
admin.site.register(sell)
admin.site.register(client)
admin.site.register(warranty)
admin.site.register(warrantycenter)