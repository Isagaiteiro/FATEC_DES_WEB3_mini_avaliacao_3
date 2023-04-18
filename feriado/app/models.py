from django.db import models


#Classe que representa a tabela no BD
class FeriadoModel(models.Model):
    id = models.AutoField(primary_key=True)
    nome_feriado = models.CharField(max_length=100)
    dia = models.IntegerField(max_length=2)
    mes = models.IntegerField(max_length=2)
    modificado_em = models.DateField(auto_now=True)
    
#Renomeando a Tabla
class Meta:
    db_table = 'feriados'
    
    def __str__(self):
        return self.nome_feriado