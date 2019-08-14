"""django_intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from pages import views # 생성한 app pages 폴더 안의 views.py 파일

urlpatterns = [
    path('isitgwangbok/', views.isitgwangbok),
    path('template_language/', views.template_language),
    path('area/<int:radius>/', views.area),
    path('times/<int:number1>/<int:number2>/', views.times),
    path('hello/<str:name>/', views.hello), # str: 은 defaul값이기 때문에 생략 가능
    path('image/', views.image),
    path('dinner/', views.dinner),
    path('introduce/<str:name>/<int:age>/', views.introduce),
    path('index/', views.index), # url 경로 마지막에 '/'를 붙이는 습관
    path('admin/', admin.site.urls),
]
