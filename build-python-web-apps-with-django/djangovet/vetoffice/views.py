from django.shortcuts import render

def home(request):
  context = {"name": "Spot"}
  return render(request, 'vetoffice/home.html', context)