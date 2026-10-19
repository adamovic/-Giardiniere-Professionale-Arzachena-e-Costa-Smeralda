from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import ContactMessage, Project
from .forms import ContactForm


def home(request):
    """Vista principale con informazioni personali"""
    projects = Project.objects.all()[:6]  # Mostra ultimi 6 progetti
    context = {
        'projects': projects,
    }
    return render(request, 'core/home.html', context)


def gallery(request):
    """Galleria completa dei progetti"""
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request, 'core/gallery.html', context)


def contact(request):
    """Form di contatto"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Salva sempre il messaggio nel database
            contact_message = form.save()
            
            # Prepara il messaggio email
            subject = f"Nuovo messaggio da {contact_message.name}"
            message = f"""
Nome: {contact_message.name}
Email: {contact_message.email}
Telefono: {contact_message.phone}
Messaggio: {contact_message.message}
"""
            
            try:
                # Prova a inviare l'email
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.DEFAULT_FROM_EMAIL],  # Invia a te stesso
                    fail_silently=False,
                )
                messages.success(request, 'Messaggio inviato con successo! Ti contatterò presto.')
                
            except Exception as e:
                # Se l'email fallisce, i dati sono già salvati nel database
                messages.warning(request, f'Messaggio salvato! Errore email: {str(e)}. Ti contatterò comunque.')
            
            return redirect('core:contact')
    else:
        form = ContactForm()
    
    return render(request, 'core/contact.html', {'form': form})
