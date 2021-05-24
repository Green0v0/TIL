from django.shortcuts import render

# Create your views here.
# generic 내에
# CRUD : Create, Read, Update, Delete
# List

# 클래스형 뷰, 함수형 뷰
# 웹 페이지에 접속한다 = 페이지를 본다
# URL을 입력 -> 웹 서버가 뷰를 찾아서 동작시킨다 -> 응답
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Bookmark # admin에서 했던 것처럼
# Ctrl + ListView(클릭)으로 내부 소스코드 살펴보기

# "상속받아서 사용한다"고 생각해라
# generic view는 기본적으로 '어떤 모델에 대한 generic view야?' 라는 것을 지정해야 한다.
# 웹 서버가 응답할 리스트 뷰를 만든 것
class BookmarkListView(ListView):
    model = Bookmark

class BookmarkCreateView(CreateView):
    model = Bookmark # 어떤 모델을 다룰 것이냐
    fields = ['site_name', 'url'] # 해당 모델의 어떤 항목들을 수정할 것이냐
    # reverse_lazy : URL pattern이름을 가지고 URL을 만들어준다
    # name space는 다음에
    success_url = reverse_lazy('list')
    # update랑 create는 기본적으로 bookmark/bookmark_form.html 기본
    # 뒤의 이름을 bookmark/bookmark_create.html으로 변경하는 코드
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'
    # success_url을 다른 방식으로 구현 = get_abolute_url (models에 적용)

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')