# polls/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice

# Create your views here.
# 질문 목록을 보여주는 View
# View 로직 순서
# 1. 사용자가 보내준 값(있다면)에 대한 검증/타입변경.
# 2. Business Logic 처리.
# 3. 결과응답

# http://127.0.0.1:8000/polls/list
def list(request):
    # business logic -> 질문을 DB 조회
    question_list = Question.objects.all().order_by('-pub_date')
    # print(question_list)
    # """
    #     <html>
    # """
    # return HttpResponse(str(question_list))

    # template을 호출 - render(request, "template의 경로" [, template에 전달할 값-dictionary]) 

    return render(request, "polls/list.html", {"question_list": question_list})

# vote_form View(한개 질문에 대한 정보를 조회해서 응답.)
def vote_form(request, question_id):
    print("vote_form", question_id)
    # question_id 질문 조회
    try:
        question = Question.objects.get(pk=question_id)

        return render(request, "polls/vote_form.html", {"question": question})
    except:
        return render(request, 'polls/error.html',{"error_message": "없는 질문을 조회하셨습니다."})