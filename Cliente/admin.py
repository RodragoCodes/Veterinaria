from django.contrib import admin
from Cliente.models import cliente, procedimientos, mascotas

# Register your models here.

admin.site.register(cliente)
admin.site.register(procedimientos)
admin.site.register(mascotas)