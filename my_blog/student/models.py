import email
from django.db import models



class Student(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return f"Nombre completo: {self.name} {self.apellido} | email: {self.email}"
# Create your models here.
