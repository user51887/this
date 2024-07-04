from django.db import models
import datetime

TITLE_CHOICES = [
     ('consultation', 'Consultation'),
    ('soins dentaire urgents', 'Soins dentaire urgents'),
    
]

# Create your models here.
class Rend(models.Model):
    nom = models.CharField( max_length=40)
    courriel = models.EmailField( max_length=50)
    choix = models.CharField(max_length=100, default="non")
    téléphone = models.IntegerField(null=True)
    
    Raison = models.CharField(max_length=50, choices=TITLE_CHOICES, null=True)
    La_Date = models.DateField(("Date"), default=datetime.date.today)
    


    def __str__(self):
        return self.nom