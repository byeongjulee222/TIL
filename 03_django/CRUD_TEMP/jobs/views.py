from django.shortcuts import render
from faker import Faker
import requests
from .models import Job
from pprint import pprint
from decouple import config

# Create your views here.

def index(request):
    return render(request, 'jobs/index.html')


def past_life(request):
    # 사용자로부터 이름 데이터를 받음.
    name = request.POST.get('name')

    # DB에 매칭되는 name 가져오기
    '''
    get이 간단하지만 이름이 없을 경우 에러를 발생하기 때문에 사용하지 않음.
    Job.objects.get(name=name)
    '''
    # filter 함수 사용
    # 한개던 0개던 상관없이 무조건 쿼리셋으로 가져옴.(리스트 형식)
    person = Job.objects.filter(name=name).first()

    # DB에 person이 있는지 없는지 판단
    if person:
        past_job = person.past_job
    else: # DB에 기존 이름이 없다면(person이 빈 쿼리셋(==False))
        faker = Faker()
        past_job = faker.job()
        person = Job(name=name, past_job=past_job)
        person.save()

    # GIPHY (past_job을 API에 요청을 보내서 응답을 받음)
    GIPHY_API_KEY = config('GIPHY_API_KEY')
    # 키값 .env로 숨겨서 가져오기
    url = f'http://api.giphy.com/v1/gifs/search?api_key={GIPHY_API_KEY}&q={past_job}&limit=1'
    data = requests.get(url).json()
    # pprint(data)
    # 이미지 없을 때 처리
    try:
        image = data.get('data')[0].get('images').get('original').get('url')
    except IndexError:
        image = None
    context = {'person': person, 'image': image,}
    return render(request, 'jobs/past_life.html', context)
