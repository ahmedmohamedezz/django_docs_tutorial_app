from django.http import HttpResponse


def index(request):
    return HttpResponse("Hi, from polls index")
