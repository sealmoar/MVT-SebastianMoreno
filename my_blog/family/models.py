import email
from django.db import models



class Family(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    birth_day = models.DateField()

    def __str__(self):
        return f"Nombre completo: {self.name} {self.last_name} | email: {self.email} | Cumpleaños: {self.birth_day}"
