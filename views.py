from ajango.http import HttpResponse


def index(request):
    return HttpResponse('index')
