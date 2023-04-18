from django.db import models


#Classe que representa a tabela no BD
class FeriadoModel(models.Model):
    id = models.AutoField(primary_key=True)
    nome_feriado = models.CharField(max_length=100)
    dia = models.IntegerField('dia')
    mes = models.IntegerField('mes')
    modificado_em = models.DateField(auto_now=True)
    
#Renomeando a Tabela
class Meta:
    db_table = 'feriados'
    
    def __str__(self):
        return self.nome_feriado