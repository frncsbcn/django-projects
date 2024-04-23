from iscrizioni.models import Studente, Insegnamento


def erase_db():
    Studente.objects.all().delete()
    Insegnamento.objects.all().delete()


def init_db():
    if Studente.objects.all().count() > 0:
        return

    studenti = [
        ("Mario", "Bianchi"),
        ("Luigi", "Verdi"),
        ("Giovanni", "Rossi"),
        ("Maria", "Viola"),
        ("Antonia", "Azzurri")
    ]

    insegnamenti = [
        "Programmazione a Oggetti",
        "Programmazione Mobile",
        "Tecnologie Web",
        "Cloud and Edge Computing",
        "Internet, Web e Cloud",
    ]

    for s in studenti:
        studente = Studente()
        studente.nome = s[0]
        studente.cognome = s[1]
        studente.save()

    for index, ins in enumerate(insegnamenti):
        insegnamento = Insegnamento()
        insegnamento.titolo = ins
        insegnamento.save()

        if index == 0:
            continue

        studenti = Studente.objects.all()
        count = 0
        for s in studenti:
            insegnamento.studenti.add(s)
            count += 1
            if count > index:
                break
