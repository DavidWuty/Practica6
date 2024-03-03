from django.contrib import admin
from .models import Carros
from .models import Motos
from .models import Bicis

# Register your models here.

admin.site.register(Carros)
admin.site.register(Motos)
admin.site.register(Bicis)