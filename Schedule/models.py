from django.db import models


class Room(models.Model):
    rooms = ((1,'Sala 1'),(2,'Sala 2'), (3, 'Sala 3'), (4, 'Sala 4'), (5, 'Sala 5'),)
    number = models.IntegerField(choices=rooms)
    name = f'Sala {number}'

    def __str__(self):
        return self.nome


class Doctor(models.Model):
    nome = models.CharField(max_length=35)
    especialidade = models.CharField(max_length=18)
    crm = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f'{self.nome}|{self.crm}'
