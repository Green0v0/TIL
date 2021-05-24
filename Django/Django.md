# Django
`pip install django`
`python manage.py startproject config .`
## template
- 화면 구성
    - html, css, javascript
## views.py
- 탬플릿 생성, 계산, 검색 결과 (in server)
## models.py
- DB를 관리해주는 중간자
- ORM을 사용하기 위한 목적이다
    - SQL을 사용하지 않고도 DB를 사용하도록
    - DB를 객체화 class화
## admin.py
- 우리가 만든 모델을 장고에 기본으로 있는 관리자 페이지에 관리하기 위해 등록 목적
## apps.py
- app에 대한 각자 설명들이 있다.
- 나중에 custom signal을 만들고, 시그널을 불러오는 역할을 추가
## \__init\__.py
- app(bookmark)자체를 패키지폴더로 인식하기 위해 있어야 하는 폴더
## test.py
- 나중에 test를 해서 추가하거나 변경했을 때, 코드로 기능들을 실험

### asgi

### urls

### wsgi

### 서버 시작, 종료
- `해당 경로>python manange.py runserver`
- Ctrl + C

### migrate
- 데이터베이스를 sqlite가 아닌 다른 것을 쓴다면 해당 DB세팅 후에
migrate와 create superuser를 해야한다.<br>
- `python manage.py migrate`
### 관리자 계정
- `python manage.py createsuperuser`
- admin, admin12345
### app
- app을 만든 것은 google store에서 다운받은 것일 뿐
- 모든 app은 `config>settings.py`에 INSTALLED_APPS에 등록해야 한다
#### bookmark
- `pyhon manage.py startapp bookmark`


### ETC
- `python mang..` tab을 누르면 자동완성