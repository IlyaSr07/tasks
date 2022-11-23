from django.http import HttpResponse

def index(request):
    return HttpResponse("Banana")

# Create your views here.
