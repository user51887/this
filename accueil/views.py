
from django.shortcuts import render , redirect
from accueil.forms import RendForm
from blog.models import Post
from services.models import Services
from equipes.models import Equipes
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse , HttpResponseRedirect


def accueil(request):
    # Check the form is submitted or not


   posts = Post.objects.all()
   services = Services.objects.all()
   service_list = Services.objects.all()
   posts = Post.objects.all()
   post_list = Post.objects.all()
   equipes = Equipes.objects.all()
   equipe_list = Equipes.objects.all()
   rendez_vous = RendForm()

   if request.method == 'POST' :
        rendez_vous = RendForm(request.POST, request.FILES)

        if rendez_vous.is_valid():

            

            nom = rendez_vous.cleaned_data['nom']
            courriel = rendez_vous.cleaned_data['courriel']
            choix = rendez_vous.cleaned_data['choix']
            
            
            
            


            
            rendez_vous.save()
            try : 
                send_mail(nom,choix,courriel,['admin@example.com'])

            except BadHeaderError:    
                return HttpResponse('ivalid header')
            return redirect('accueil:send_success')   

        else: 
          rendez_vous = RendForm()


   context = {  
                'form' : rendez_vous,
                'services' : services,
                'service_list' : service_list,
                'posts' : posts,
                'post_list' : post_list ,
                'equipes' : equipes,
                'equipe_list' : equipe_list ,
              }

   return render(request , 'accueil/index.html' , context)


def send_success(request):
    context = {
        'send_success' : send_success
    }
    return render(request , 'accueil/send_success.html' , context)
    


    



   