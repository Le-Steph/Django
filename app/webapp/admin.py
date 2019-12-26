from django.contrib import admin
from .models import farmer
from .models import product
from .models import certificate
# Register your models here.


admin.site.register(farmer)
admin.site.register(product)
admin.site.register(certificate)