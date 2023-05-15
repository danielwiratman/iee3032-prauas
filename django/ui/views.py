from django.shortcuts import render

def index(request):
    return render(request, 'ui/index.html')

# Create your views here.
# create a new view returning a json response


