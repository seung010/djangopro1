"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# 장고디렉터리내의 urls 내의 path라는 기능을 이용해서 패턴정의를 함
# include를 통해 계층구조를 만들 것이다.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('MTV/', include('MTV.urls')),
    # 사이트주소/MTV라는 url request가 들어온다면 ,뒤를 호출(MTV디렉터리 내의 urls 파일) <- 계층적 구조
]
