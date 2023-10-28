from django.db import models


class Secundario(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    createDate = models.DateTimeField(auto_now_add=True, null=False, blank=False) #criação
    deadLine = models.DateTimeField(null=False, blank=False) #previsão pra entrega
    finishedDate = models.DateTimeField(null=False) #entrega
    