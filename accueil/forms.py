# Import form modules
from django import forms

from accueil.models import TITLE_CHOICES, Rend
from functools import partial

DateInput = partial(forms.DateInput, {'class': 'datepicker'})

CHOICES = [
 ('Oui', 'oui'),
 ('Non', 'non')
]


class DateInput(forms.DateInput):
    input_type = 'date'

# Create class to define the form fields
class RendForm(forms.ModelForm):
    nom = forms.CharField(label="nom complet", max_length=40)
    courriel = forms.EmailField(label="courriel", max_length=50)
    choix = forms.ChoiceField(label='Etes-vous déjà patient à notre cabinet?', choices=CHOICES)
    téléphone = forms.IntegerField()
    
    Raison = forms.ChoiceField(label='Raison de votre visite :', choices=TITLE_CHOICES)
    
  

    



    def __str__(self):
        return self.nom


    class Meta:
          model = Rend  
          fields = ['nom', 'courriel','choix','téléphone','Raison','La_Date']
          widgets = {
            'La_Date': DateInput(),
        }