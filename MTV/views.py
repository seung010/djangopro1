from django.shortcuts import render
from django.http import HttpResponse
#위 코드는 Response메시지를 만들어서 views의 부름에 응답을 해주겠다는 의미


# Create your views here.
#views에서 다이렉트로 연결되는 구조는 거의 존재하지 않는다

def index(request):
    #현재 매개변수로 request를 적지 않아도 되지만 함수를 선언할 때 무조건 request를 적어야한다 
    #request에는 client 요청 정보가 모두 들어가 있다
    # 위 정보를 if문에 따라 request 속의 메시지에 따라 응답해야하는 페이지가 달라지기 때문에 
    print(request)
    #request에 무엇이 들어있는지 궁금할 때 사용, 터미널창에만 print가 찍혀나옴
    return HttpResponse("Hello, World. Django MTV App Index Page!")
    #HttpResponse : request이 온 쪽으로 값을 전송,5,6,7계층에서의 헤더세팅이 "자동"으로 됨 
def lang(request,lang):
    #매개변수 Lang에 앞의 <lang>이 저장됨.
    lang_code = {'ko':'korean','en':'english'}
    if lang_code.get(lang):
        message = f'{lang_code.get(lang)} Page!'
    else:
        message = f'{(lang)} Not Found!'
    return HttpResponse(message)
        
def num(request,num):
    num_lst=[1,2,3,4,5]
    if num in num_lst:
        message = f'Numbers : {num}'
    else:
        message = f'Numbers : {num} Not Found!'
    return HttpResponse(message)