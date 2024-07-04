from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    
   
    
    sujet = forms.CharField()

    email = forms.CharField(required = True)
    
    message = forms.CharField(widget=forms.Textarea , required = True)


    def __str__(self):
        return self.sujet

    class Meta:
          model = Contact
          fields = ['sujet', 'email','message']