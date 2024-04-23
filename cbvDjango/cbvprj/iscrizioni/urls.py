"""
URL configuration for cbvprj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from iscrizioni import views
app_name = "iscrizioni"

urlpatterns = [
    path('listastudenti/', views.ListaStudenti.as_view(), name='listastudenti'),
    path('listainsegnamenti/', views.ListaInsegnamenti.as_view(), name='listainsegnamenti'),
    path('insegnamentiattivi/', views.ListaInsegnamentiAttivi.as_view(), name='insegnamentiattivi'),
    path('creastudente/', views.CreaStudente.as_view(), name='creastudente'),
    path('creainsegnamento/', views.CreaInsegnamento.as_view(), name='creainsegnamento'),
    path('insegnamento/<pk>', views.DetailInsegnamento.as_view(), name='insegnamento'),
    path('updateinsegnamento/', views.UpdateInsegnamento.as_view(), name='updateinsegnamento'),
    path('cancellastudente/', views.DeleteStudente.as_view(), name='cancellastudente'),
    path('cancellainsegnamento/', views.DeleteInsegnamento.as_view(), name='cancellainsegnamento'),
    path('studente/<str:cognome>/', views.StudentePerCognome.as_view(), name='studente'),
    path('cercastudenti/', views.cerca_studenti, name='cercastudenti'),
    path('cercastudenti/<str:nome>/<str:cognome>/', views.StudentiConInsegnamento.as_view(), name='studenti'),
]
