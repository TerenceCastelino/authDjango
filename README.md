# Django Auth Starter (Custom User) — Windows CMD

Un squelette **Django 5** prêt à l’emploi avec : utilisateur personnalisé, inscription, connexion, **logout en POST**, changement et **réinitialisation** de mot de passe, pages protégées.

## 🚀 Quickstart (Windows CMD)

```bat
:: 0) créer/entrer dans le dossier projet
mkdir django-auth-demo && cd django-auth-demo

:: 1) venv
py -m venv ENV
ENV\Scripts\activate.bat

:: 2) install
pip install -r requirements.txt  ||  pip install "Django>=5,<6"

:: 3) projet + app
py -m django startproject mysite .
python manage.py startapp accounts

:: 4) migrations & admin
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

:: 5) run
python manage.py runserver
```
- Accès : `/accounts/signup/`, `/accounts/login/`, `/accounts/password_change/`, `/accounts/password_reset/`

## 🧱 Structure attendue (résumé)

```
mysite/
  settings.py  urls.py  ...
accounts/
  models.py  forms.py  views.py  admin.py  urls.py
templates/
  base.html  home.html
  registration/
    login.html
    signup.html
    password_change_form.html
    password_change_done.html
    password_reset_form.html
    password_reset_done.html
    password_reset_confirm.html
    password_reset_complete.html
```

## 👤 Custom User

`accounts/models.py` :
```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """Extensible (ajoute tes champs plus tard)."""
    pass
```

`mysite/settings.py` :
```python
AUTH_USER_MODEL = "accounts.User"
TEMPLATES[0]["DIRS"] = [BASE_DIR / "templates"]
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "login"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
```

## 🧭 URLs

`mysite/urls.py` :
```python
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
]
```

`accounts/urls.py` :
```python
from django.urls import path
from .views import SignUpView

app_name = "accounts"
urlpatterns = [ path("signup/", SignUpView.as_view(), name="signup") ]
```

## 📝 Templates clés

- `base.html` : inclure un **formulaire POST** pour `/accounts/logout/` (Django 5 n’accepte plus GET).
```html
<form method="post" action="{% url 'logout' %}" style="display:inline">
  {% csrf_token %}
  <button type="submit" style="background:none;border:none;padding:0;text-decoration:underline">Se déconnecter</button>
</form>
```
- `registration/signup.html` : formulaire d’inscription.
- `registration/login.html` : connexion (+ lien vers `{% url 'password_reset' %}`).
- Les 5 templates de reset/change fournis.

## 🧩 Formulaire & Vue d’inscription

`accounts/forms.py` :
```python
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")
```

`accounts/views.py` :
```python
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
```

## 🩺 Dépannage rapide

- **NoReverseMatch 'signup'** → avec `app_name = "accounts"`, utilise `{% url 'accounts:signup' %}`.
- **405 sur `/accounts/logout/`** → faire **POST** (voir `base.html` ci-dessus).
- **`{% extends %} must be first`** → mettre `{% extends 'base.html' %}` tout en haut du template.
- **Password validators custom ImproperlyConfigured** → corriger le chemin ou retirer temporairement.

## 📦 Bonus

Créer vite fait les fichiers :
```bat
(echo Django==5.2.6) > requirements.txt

(
echo ENV/
echo __pycache__/
echo *.py[cod]
echo db.sqlite3*
echo staticfiles/
echo media/
echo .env
echo .vscode/
echo .idea/
echo .DS_Store
echo Thumbs.db
) > .gitignore
```

---

**Licence** : libre au choix (MIT recommandé).
