from django.db import models

class Genero(models.Model):
   id = models.AutoField(primary_key=True)
   nome = models.CharField(max_length=50)

   def __str__(self):
      return self.nome

class Diretor(models.Model):
   id = models.AutoField(primary_key=True)
   nome = models.CharField(max_length=50)

class Filme(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT)
    duracao = models.IntegerField()
    ano = models.IntegerField()
    diretor = models.CharField(max_length=100)
    sinopse = models.TextField(blank=True, null=True)
    poster = models.ImageField(upload_to='posters/', null=True,blank=True)
    
    def __str__(self):
      return self.titulo
