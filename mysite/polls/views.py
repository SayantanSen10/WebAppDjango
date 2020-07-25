from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. 1fb2a1c3 is the polls index.")
