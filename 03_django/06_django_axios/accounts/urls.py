from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='change_password'),
    # 문자열만 있는 주소를 입력할 때는 최하단에 입력해야한다. (위에 있으면 아래에 있는 주소를 읽지 못함.)
    path('<str:username>', views.profile, name='profile'),
]
