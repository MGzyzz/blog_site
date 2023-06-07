from django.shortcuts import render


# Create your views here.
def home_page(request):
    return render(request, 'pages/home.html')


def fist_page(request):
    return render(request, 'pages/first_page.html')


def second_page(request):
    return render(request, 'pages/second_page.html')