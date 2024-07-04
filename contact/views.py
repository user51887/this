from django.shortcuts import render , redirect
from django.core.mail import send_mail , BadHeaderError
from django.http import HttpResponse , HttpResponseRedirect
from .forms import ContactForm
# Create your views here.


def send_email(request):

    form = ContactForm()

    if request.method == 'POST' :
        
        form = ContactForm(request.POST, request.FILES)

        if form.is_valid():
              
            
            sujet = form.cleaned_data['sujet']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            form.save()
            try : 
                send_mail(sujet,message,email,['admin@example.com'])


            except BadHeaderError:    
                return HttpResponse('ivalid header')

                

            return redirect('contact:send_success')    
                
    else:    

        form = ContactForm()

    context = {
        'form' : form
    }

    return render(request , 'contact/contact.html' , context)

def send_success(request):
    context = {
        'send_success' : send_success
    }
    return render(request , 'contact/send_success.html' , context)
