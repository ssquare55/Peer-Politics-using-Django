from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import datetime
    import json
    now = datetime.date.today()
    api_request = requests.get("https://newsapi.org/v2/everything?q=politics&from="+str(now)+"&sortBy=publishedAt&apiKey=233a8b7ce93443c0b5babf55818f24dc")
    api = json.loads(api_request.content)
    return render(request,'home.html',{'api':api,'now':now})

def headline(request):
    import requests
    import json
    headline_api = requests.get("https://newsapi.org/v2/top-headlines?sources=google-news&apiKey=233a8b7ce93443c0b5babf55818f24dc")
    headapi = json.loads(headline_api.content)
    return render(request,'headlines.html',{'headapi':headapi})

def business(request):
    import requests
    import json
    business_api = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=233a8b7ce93443c0b5babf55818f24dc")
    businessapi = json.loads(business_api.content)
    return render(request,'business.html',{'businessapi':businessapi})


def technology(request):
    import requests
    import json
    technology_api = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=233a8b7ce93443c0b5babf55818f24dc")
    technologyapi = json.loads(technology_api.content)
    return render(request,'technology.html',{'technologyapi':technologyapi})


def entertainment(request):
    import requests
    import json
    entertainment_api = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=233a8b7ce93443c0b5babf55818f24dc")
    entertainmentapi = json.loads(entertainment_api.content)
    return render(request,'entertainment.html',{'entertainmentapi':entertainmentapi})


def health(request):
    import requests
    import json
    health_api = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=233a8b7ce93443c0b5babf55818f24dc")
    healthapi = json.loads(health_api.content)
    return render(request,'health.html',{'healthapi':healthapi})


def science(request):
    import requests
    import json
    science_api = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=233a8b7ce93443c0b5babf55818f24dc")
    scienceapi = json.loads(science_api.content)
    return render(request,'science.html',{'scienceapi':scienceapi})


def sports(request):
    import requests
    import json
    sports_api = requests.get("https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=233a8b7ce93443c0b5babf55818f24dc")
    sportsapi = json.loads(sports_api.content)
    return render(request,'sports.html',{'sportsapi':sportsapi})


def answer(request):
    import requests
    import json
    import datetime
    now = datetime.date.today()
    if request.method == 'POST':
        value = request.POST['ask']
        answer_api = requests.get("https://newsapi.org/v2/everything?q="+value+"&from="+str(now)+"&sortBy=publishedAt&apiKey=233a8b7ce93443c0b5babf55818f24dc")
        answerapi = json.loads(answer_api.content)
        return render(request,'answer.html',{'answerapi':answerapi})
    else:
        answerapi = 'error processing this request'
        return render(request,'answer.html',{'answerapi':answerapi})
