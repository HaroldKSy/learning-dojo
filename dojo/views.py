from django.shortcuts import render
from .questions import get_random_question

def dojo_view(request):
    result = None

    if request.method == "POST":
        question_text = request.POST.get("question")
        correct_answer = request.POST.get("correct_answer")
        user_answer = request.POST.get("answer")
        

        if user_answer == correct_answer:
            result = "Correct!"
        else:
            result = "Wrong!"

        question = {"text": question_text, "answer": correct_answer}


    else: # GET
        question = get_random_question()

    return render(request, "dojo/dojo.html", {"question": question,"result": result})


