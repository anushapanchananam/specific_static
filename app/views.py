from django.shortcuts import render

# Create your views here.


def daddy(request):
    return render(request, 'daddy.html')