from django.contrib import admin
from .models import Question, Choice
# 현재 경로에 있는 models를 import하겠다.
# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)