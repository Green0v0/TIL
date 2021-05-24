# 2차 url
from django.urls import path
from .views import *

urlpatterns = [
    # http://127.0.0.1/bookmark/??? > ???를 맡는다
    # 클래스형의 경우 .as_view()를 반드시 해야 한다
    # .as_view()를 통해 클래스 뷰가 함수형 뷰로 전환된다.
    # 내부적으로 함수형 뷰로 대부분을 처리한다
    # name='list'는 (화면을 보여줄)템플릿에서 해당 URL을 불러다가 쓸 때 사용
    # 즉, URL pattern의 이름이라고 생각하면 된다
    path("", BookmarkListView.as_view(), name='list'),
    path("add/", BookmarkCreateView.as_view(), name='add'),
    # <int:pk> 해당 글의 글번호를 보여줘라 pk = primary key
    # <pk>면 문자열로 들어감 or 슬러그도 사용 가능하다
    path("detail/<int:pk>/", BookmarkDetailView.as_view(), name='detail'),
    path("update/<int:pk>/", BookmarkUpdateView.as_view(), name='update'),
    path("delete/<int:pk>/", BookmarkDeleteView.as_view(), name='delete'),
]