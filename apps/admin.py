
from django.contrib import admin
from django.contrib.auth.models import Group

from apps.models import Product, User


admin.site.unregister(Group)

admin.site.register(Product)
admin.site.register(User)
