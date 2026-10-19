from django.db import models
from django.utils import timezone


class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Telefono")
    message = models.TextField(verbose_name="Messaggio")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data di invio")

    class Meta:
        verbose_name = "Messaggio di contatto"
        verbose_name_plural = "Messaggi di contatto"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.email}"


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titolo")
    description = models.TextField(verbose_name="Descrizione")
    image = models.ImageField(upload_to='projects/', verbose_name="Immagine")
    before_image = models.ImageField(upload_to='projects/before/', blank=True, null=True, verbose_name="Immagine prima")
    after_image = models.ImageField(upload_to='projects/after/', blank=True, null=True, verbose_name="Immagine dopo")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data di creazione")

    class Meta:
        verbose_name = "Progetto"
        verbose_name_plural = "Progetti"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
