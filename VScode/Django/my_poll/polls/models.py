from django.db import models

# Create your models here.
# Question(질문)
#   - question_text(질문내용)
#   - pub_data(질문 등록일시)
#   - id(PK - 자동생성): 1씩 증가하는 값을 가지도록 자동생성
# Choice(선택지)
#   - choice_text(보기내용)
#   - vote(몇 번 선택되었는지)
#   - question(어떤 질문에 대한 보기인지 - Question의 Foreign key 컬럼)
#   - id(PK - 자동생성): 1씩 증가하는 값을 가지도록 자동생성

# Model을 상속
# 컬럼과 연결된 Field들을 class 변수로 선언
class Question(models.Model):
    # 변수명 : 컬럼명
    # 값 : Field 객체대입 -> 타입을 알려준다.

    # CharField == NVACHAR
    question_text = models.CharField(max_length=200)
    # auto_now_add : insert될 때 일시를 자동등록(insert)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return self.quest_text
        return self.question_text
    
    # class Meta:
    #     ordering = ['pub_date']

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    vote = models.PositiveIntegerField(default=0) # 0과 양수만 적용
    # to : 참조 Model 클래스(=테이블) 지정.
    # on_delete : 부모테이블의 값이 delete될 경우 처리방식.
    #   - CASCADE : 참조하는 자식데이터도 같이 삭제하겠다.
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text