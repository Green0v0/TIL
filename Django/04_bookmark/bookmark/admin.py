from django.contrib import admin

# Register your models here.
# 내가 만든 모델을 관리자 페이지에서 관리할 수 있도록 등록
# .(현재 패키지)의 models에서 bookmark를 불러오겠다
from .models import Bookmark

# 등록
admin.site.register(Bookmark)