from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    # Otros campos personalizados aquí, si los tienes

    # Define 'related_name' para evitar el conflicto
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Cambia 'custom_user_set' por lo que prefieras
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # Cambia 'custom_user_permissions_set' por lo que prefieras
        blank=True
    )

class Semestre(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title}"

# -------------------------------------------------------------
class Categoria_Clase(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title}"

# ---------------------------------------------------------------
class Categoria_Evaluacion(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title}"
    
# ---------------------------------------------------------------
class Clase(models.Model):
    title = models.CharField(max_length=100)
    teacher = models.CharField(max_length=50)
    id_category = models.ForeignKey(Categoria_Clase, on_delete=models.CASCADE, verbose_name='categoria_clase')
    id_semester = models.ManyToManyField(Semestre, through='ClaseSemestre',verbose_name='semestre')

    def __str__(self):
        return f"{self.title} {self.teacher}"

# ---------------------------------------------------------------
class ClaseSemestre(models.Model):  # Modelo intermedio con tipo de curso
    course = models.ForeignKey(Clase, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semestre, on_delete=models.CASCADE)
    id_category = models.ForeignKey(Categoria_Clase, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.clase.title}  {self.semestre.title}  {self.categoria_clase.title}"   
# ------------------------------------------------------------------
class Evaluacion(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_evaluation = models.DateField()
    calification = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    score_obtained = models.DecimalField(default=0, decimal_places=2, max_digits=6, null=True, blank=True)
    id_category = models.ForeignKey(Categoria_Evaluacion, on_delete=models.CASCADE, verbose_name='categoria_evaluacion')
    id_class = models.ForeignKey(Clase, on_delete=models.CASCADE, verbose_name='clase')

    def __str__(self):
        return f"{self.title}  {self.date_evaluation} {self.calification}"
    
    


   
    



    