from django.db import models

class Event(models.Model):
    priorities_list = (
        ('0', 'Sem prioridade'),
        ('1', 'Normal'),
        ('2', 'Urgente'),
        ('3', 'Muito urgente'),
        ('4', 'Ultra Mega Hiper Urgente')
    )

    date = models.DataField(max_length=100)
    event = models.CharField(max_length=1)
    priority = models.CharField(max_length=1, choices=priorities_list)

    def __str__(self):
        return self.event