from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import *


class ListaStudenti(ListView):
    model = Studente
    template_name = 'iscrizioni/lista.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titolo"] = "Studenti"
        return context


class ListaInsegnamenti(ListView):
    model = Insegnamento
    template_name = 'iscrizioni/insegnamenti.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titolo"] = "Insegnamenti"
        return context


class ListaInsegnamentiAttivi(ListView):
    model = Insegnamento
    template_name = 'iscrizioni/lista.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titolo"] = "Insegnamenti attivi"
        return context

    def get_queryset(self):
        return self.model.objects.exclude(studenti__isnull=True)


class CreaStudente(CreateView):
    model = Studente
    template_name = 'iscrizioni/crea.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titolo"] = "Crea studente"
        return context

    def get_success_url(self):
        return reverse('iscrizioni:lista')


class CreaInsegnamento(CreateView):
    model = Insegnamento
    template_name = 'iscrizioni/crea.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titolo"] = "Crea insegnamento"
        return context

    def get_success_url(self):
        return reverse('iscrizioni:insegnamenti')


class DetailInsegnamento(DetailView):
    model = Insegnamento
    template_name = 'iscrizioni/insegnamento.html'


class UpdateInsegnamento(UpdateView):
    model = Insegnamento
    template_name = 'iscrizioni/update.html'
    fields = '__all__'

    def get_success_url(self):
        pk = self.get_context_data()["object"].pk
        return reverse('iscrizioni:insegnamento', kwargs={'pk': pk})


class Delete(DeleteView):
    template_name = 'iscrizioni/cancella.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["oggetto"] = "studente"
        if self.model == Insegnamento:
            context["oggetto"] = "insegnamento"
        return context

    def get_success_url(self):
        if self.model == Insegnamento:
            return reverse('iscrizioni:listainsegnamenti')
        return reverse('iscrizioni:listastudenti')


class DeleteStudente(Delete):
    model = Studente


class DeleteInsegnamento(Delete):
    model = Insegnamento


class StudentePerCognome(ListaStudenti):
    def get_queryset(self):
        cognome = self.kwargs["cognome"]
        return self.model.objects.filter(cognome__iexact=cognome)


class StudentiConInsegnamento(ListView):
    model = Studente
    template_name = 'iscrizioni/studenti.html'

    def get_queryset(self):
        try:
            nome = self.kwargs["nome"]
            query_nome = self.model.objects.filter(nome__iexact=nome)
        except:
            query_nome = self.model.objects.none()

        try:
            cognome = self.kwargs["nome"]
            query_cognome = self.model.objects.filter(cognome__iexact=cognome)
        except:
            query_cognome = self.model.objects.none()

        return query_nome | query_cognome

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titolo"] = "Studenti e loro insegnamenti"

        insegnamenti = set()
        for studente in self.get_queryset():
            for insegnamento in Insegnamento.objects.all():
                if studente in insegnamento.studenti.all():
                    insegnamenti.add(insegnamento)

        context["insegnamenti"] = insegnamenti
        return context


def cerca_studenti(request):
    if request.method == "GET":
        return render(request, template_name='iscrizioni/cerca_studenti.html')
    else:
        if len(request.POST["nome"]) < 1:
            nome = "null"
        else:
            nome = request.POST["nome"]

        if len(request.POST["cognome"]) < 1:
            cognome = "null"
        else:
            cognome = request.POST["cognome"]

        return redirect('iscrizioni:studenti', nome=nome, cognome=cognome)
