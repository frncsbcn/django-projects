from polls.models import *
import json
import os
import random
from pathlib import Path
from datetime import timedelta
from django.utils import timezone
import html


def erase_db():
    Question.objects.all().delete()
    Choice.objects.all().delete()


def init_db():
    if Question.objects.count() > 0:
        return

    data = None
    filepath = os.path.join(Path(os.getcwd()), "static", "questions", "questions.txt")
    with open(filepath, "r") as f:
        data = f.read()

    if data is None:
        print("Error in populating database")
        return

    data = json.loads(data)["results"]

    for i, d in enumerate(data):
        question = d["question"]

        choices = []
        choices.append(d["correct_answer"])
        choices.extend(d["incorrect_answers"])
        random.shuffle(choices)

        date = timezone.now() - timedelta(days=i%10)

        q = Question(question_text=html.unescape(question), pub_date=date)
        q.save()

        for k, j in enumerate(choices):
            c = Choice(choice_text=html.unescape(j), votes=k, question=q)
            if j == d["correct_answer"]:
                c.is_correct = True
            c.save()