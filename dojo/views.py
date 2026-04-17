from django.shortcuts import render
from .questions import get_random_question

def dojo_view(request):
    question = get_random_question()
    result = None

    if request.method == "POST":
        user_answer = request.POST.get("answer")
        correct_answer = request.POST.get("correct_answer")

        if user_answer == correct_answer:
            result = "Correct!"
        else:
            result = "Wrong!"

    return render(request, "dojo.html", {
        "question": question,
        "result": result
    })


