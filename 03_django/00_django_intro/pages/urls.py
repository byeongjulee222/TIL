from django.urls import path
from . import views # from . 을 작성하지 않아도 작동하지만 명시적으로 작성하는 것을 권장

urlpatterns = [
    # 원래 app url은 아래로 작성해나간다.
    path('index/', views.index), # url 경로 마지막에 '/'를 붙이는 습관
    path('introduce/<str:name>/<int:age>/', views.introduce),
    path('dinner/', views.dinner),
    path('image/', views.image),
    path('hello/<str:name>/', views.hello), # str: 은 defaul값이기 때문에 생략 가능
    path('times/<int:number1>/<int:number2>/', views.times),
    path('area/<int:radius>/', views.area),
    path('template_language/', views.template_language),
    path('isitgwangbok/', views.isitgwangbok),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('art/', views.art),
    path('result/', views.result),
    path('user_new/', views.user_new),
    path('user_create/', views.user_create),
    path('static_example/', views.static_example),
]
