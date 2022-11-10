from django.shortcuts import render

def apple(request):
    return render(request, 'apple.html')

def huave(request):
    return render(request, 'huave.html')

def samsung(request):
    return render(request, 'samsung.html')
