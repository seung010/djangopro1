from django.urls import path
#장고 패키지의 urls 모듈, 거기에서 path를 가져온다 = 패턴구조화를 위해
from . import views
#특정 url과 매치되는 기능이 들어있는 views(현재 앱의 views) 호출


#/MTV라는 값을 가지고 해당 파일에 접근함.
#/MTV의 뒷부분을 확인함. 뒤가 없다면 path(' '(공백),views.index)와 연결됨

app_name='MTV'
#어떤 어플리케이션의 url pattern인지 정의
urlpatterns = [
    path('',views.index),
    #path를 통해 패턴을 이용한 구조화
    #MTV의 뒷부분에 공백이 온다면 views.py 안에 index정의를 해야함.
    #앞부분이 MTV이고,뒤의 부분이 ,의 앞부분이라면 views의 index함수를 실행하라.
    path('document/<lang>/',views.lang),
    #꺾쇠 내부의 값들은 변수이다, 기본형은 String - 문자열, 아래처럼 type를 설정 가능
    #document/korea로 들어온다면 korea라는 값을 String형으로 <lang>에 담아둠.
    #추가 매개변수를 보낸다고 생각하면 편하다 
    
    path('numpage/<int:num>/',views.num),
    #numpage/8로 request가 온다면 8이라는 int값을 int형으로 <num>에 담아둠
    
    
]
#list의 형태로 url patterns를 정의