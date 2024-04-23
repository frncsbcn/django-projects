from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
import logging


logger = logging.getLogger(__name__)


def home_page(request):
    response = "Benvenuto " + str(request.user)

    if not request.user.is_authenticated:
        logger.warning("User %s is not authenticated", request.user)

    print("REQUEST: ", str(request))

    return HttpResponse(response)


def elenca_params(request):
    response = ""

    for k in request.GET:
        response += request.GET[k] + " "

    return HttpResponse(response)


def pari_dispari(request):
    response = ""

    """
    ROBA CHE HO PROVATO IO
    if len(request.GET) > 1:
        response += "Troppi parametri"
        return HttpResponse(response)

    for k in request.GET:
        if not str(request.GET[k]).isnumeric():
            response += "Non è un numero"
        elif (int(request.GET[k]) % 2) == 0:
            response += "Pari"
        else:
            response += "Dispari"
    """

    # ROBA GIUSTA DEL PROF
    try:
        if int(request.GET["num"]) % 2 == 0:
            response += "Pari"
        else:
            response += "Dispari"
    except:
        response += "Non è un numero"

    return HttpResponse(response)


def saluta(request):
    response = ""
    try:
        response += "Ciao " + str(request.GET["nome"])
    except:
        response += "Nome sbagliato"

    return HttpResponse(response)


def welcome(request):
    response = ""
    response += "Welcome " + request.path[len("welcome_") + 1:]

    return HttpResponse(response)


def welcome_vars(request, name, age):
    return HttpResponse("Welcome " + name + ", " + str(age))


def hello(request):
    ctx = {"title": "hello template",
           "lista": [datetime.now(),
                     datetime.today().strftime("%A"),
                     datetime.today().strftime("%B")]}

    return render(request, "baseext.html", ctx)
