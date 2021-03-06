from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

# 사용자에게 현재(요청한) 날짜와 시간을 알려준다.
def hello1(request):
    curr = datetime.now()
    txt = """
    <html>
        <body>
            안녕하세요.<br>
            현재일시 {}입니다.
        </body>
    </html>
    """
    res_txt = txt.format(curr)
    response =  HttpResponse(res_txt)
    return response

def hello2(request):
    curr = datetime.now()
    curr_txt = curr.strftime('%Y-%m-%d %H:%M:%S')

    return render(request, "exam/greeting.html", {"current" : curr_txt})