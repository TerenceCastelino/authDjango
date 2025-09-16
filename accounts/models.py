from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Utilisateur personnalisable.
    Ajoute des champs ici si besoin (ex: téléphone, avatar, etc.).
    """
    # Exemple (activer plus tard si tu veux) :
    # phone = models.CharField(max_length=20, blank=True)
    # avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    pass
