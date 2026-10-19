from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Il tuo nome',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'La tua email',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Il tuo numero di telefono (opzionale)'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descrivi il lavoro di giardinaggio di cui hai bisogno...',
                'rows': 5,
                'required': True
            }),
        }
        labels = {
            'name': 'Nome',
            'email': 'Email',
            'phone': 'Telefono',
            'message': 'Messaggio',
        }
