from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Contact, Newsletter

# Create your views here.
def home(request):
    context = {
        'path': 'Home'
    }
    return render(request, 'pages/index.html', context)

def about(request):
    context = {
        'path': 'About'
    }
    return render(request, 'pages/about.html', context)

def service(request):
    context = {
        'path': 'Services'
    }
    return render(request, 'pages/service.html', context)

def project(request):
    context = {
        'path': 'Projects'
    }
    return render(request, 'pages/project.html', context)



def contact(request):
    
    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
       # Enregistrer les données dans la table Contact
        contact_entry = Contact(name=name, email=email, subject=subject, message=message)
        contact_entry.save()

        # Envoyer un e-mail (vous devez configurer les paramètres d'e-mail dans settings.py)
        send_mail(

            f'Sujet : {subject}',
            f'Message de {name} ({email}):\n\n{message}',

            email,  # Votre adresse e-mail
            ['maksoricheisaac@gmail.com'],  # Adresse e-mail du destinataire récupérée depuis le formulaire
            fail_silently=False,
        )
        messages.success(request, 'Votre message a été envoyé avec succès !')
        return redirect('contact')  

    context = {
        'path': 'Contact'
    }
    return render(request, 'pages/contact.html', context)

def newsletter(request):
    if request.method == "POST":
        email = request.POST.get('email')

       
        if Newsletter.objects.filter(email=email).exists():
            messages.error(request, 'Cet e-mail est déjà inscrit !')
            return redirect(request.META.get('HTTP_REFERER'))  

        newEmail = Newsletter(email=email)
        newEmail.save()
        messages.success(request, 'Email ajoutée avec succès !')
        return redirect(request.META.get('HTTP_REFERER'))  
    
    context = {
        'path': 'Newsletter'
    }
    return render(request, 'pages/newsletter.html', context)  
