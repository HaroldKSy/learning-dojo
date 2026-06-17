from django.shortcuts import render
from .questions import get_random_question

def dojo_view(request):

    result = None
    question = None

    if request.method == "POST":

        #--------------------------------------------------#
        # If user clicked "Next Question"                  #
        #--------------------------------------------------#
        if "next" in request.POST:
            question = get_random_question()
            result = None

        
        #--------------------------------------------------#
        # Otherwise, user submitted an answer              #
        #--------------------------------------------------#
        else:
            question_text = request.POST.get("question")
            correct_answer = request.POST.get("correct_answer")
            user_answer = request.POST.get("answer")
        
            #--------------------------------------------------#
            # Set variable to outcome of user answer:          #
            #--------------------------------------------------#
            if user_answer == correct_answer:
                result = "Correct!"
            else:
                result = "Wrong!"

            #--------------------------------------------------#
            # Reuse the same question and answer for HTML field#
            #--------------------------------------------------#       
            question = {
                         "question": question_text, 
                         "answer": correct_answer}

    else: 
        #--------------------------------------------------#
        # Get a new question and answer to that question   #
        #--------------------------------------------------#
        question = get_random_question()


    return render(request, "dojo/dojo.html", {"question": question,"result": result})


