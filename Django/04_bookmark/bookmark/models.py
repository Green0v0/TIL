from django.db import models
from django.urls import reverse
# Create your models here.

# 모델 : 데이터베이스를 SQL 없이 다루려고 모델을 사용
# '우리가 데이터를 객체화해서 다루겠다' 라는 의미
# 모델 = 테이블
# 모델의 필드 = 테이블의 컬럼
# 인스턴스 = 테이블의 레코드
# 필드의 값(인스턴스의 필드값) = 레코드의 컬럼 데이터값

# https://velog.io/@tbnsok40/%ED%8C%8C%EC%9D%B4%EC%8D%AC-str-init-%EB%A9%94%EC%84%9C%EB%93%9C
class Bookmark(models.Model):
    # site_name은 글자를 입력할 것이기 때문에, CharField 사용
    site_name = models.CharField(max_length=100)
    # 문자열이지만 URLField는 링크가 자동으로 걸리는 효과가 있다
    url = models.URLField('Site URL')
    # 필드의 종류가 결정하는 것
    # 1. 데이터베이스의 컬럼 종류
    # 2. 제약 사항 (몇 글자까지)
    # 3. Form의 종류
    # 4. Form에서 제약 사항

    def __str__(self): # Magic Method
        return "이름 : " + self.site_name + ", 주소 : " + self.url

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

# 모델을 만들었다 = 데이터베이스에 어떤 데이터들을 어떤 형태로 넣을지 결정했다.
# makemigrations = 모델의 변경사항을 추적해서 기록 -> migrate 할 정보가 생성
# 마이그레이션(migrate) = 데이터베이스에 모델의 내용을 반영(테이블 생성)
# 모델을 수정하고 다시 migrate해야 한다.