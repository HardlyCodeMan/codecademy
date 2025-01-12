from django.shortcuts import render

pets = [
   { 'petname': 'Fido', 'animal_type': 'dog'},
   { 'petname': 'Clementine', 'animal_type': 'cat'},
   { 'petname': 'Cleo', 'animal_type': 'cat'},
   { 'petname': 'Oreo', 'animal_type': 'dog'},
]

# Create your views here.
def home(request):
   context = {"name": "Djangoer", "pets": pets}
   return render(request, 'vetoffice/home.html', context)
