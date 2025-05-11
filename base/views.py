from django.shortcuts import render




def home(request):
    return render(request, 'base/base.html')


def pages(request):
    return render(request, 'pages/index.html')