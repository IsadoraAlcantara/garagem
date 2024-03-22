from django.db import models 


class Acessorio(models.Model):
    descricao = models.CharField(max_length=100)

    def __src__(self):
        return f"{self.descricao} ({self.id})"