from django.contrib import admin
from .models import Categoria_Clase, Categoria_Evaluacion, Semestre, Clase, Evaluacion, ClaseSemestre


# Register your models here.
admin.site.register(Categoria_Clase)
admin.site.register(Categoria_Evaluacion)
admin.site.register(Semestre)
admin.site.register(Clase)
admin.site.register(Evaluacion)
admin.site.register(ClaseSemestre)
