from django.shortcuts import render
from django.http import HttpResponse

class Dog: 
  def __init__(self, name, breed, size, color, characteristics, age):
    self.name = name
    self.breed = breed
    self.size = size
    self.color = color
    self.characteristics = characteristics
    self.age = age

dogs = [
  Dog('Kobe', 'maltese', 'small', 'black', 'high energy', 0),
  Dog('Bailey', 'maltipoo', 'medium', 'brown', 'sweet nad mild tempered', 1),
  Dog('JoJo', 'labrador', 'large', 'golden', 'loyal, likes to play fetch', 3),
]

def home(request):
  return HttpResponse('<h1>Hello Welcome To: The Dog Collector')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
  return render(request, 'dogs/index.html', { 'dogs': dogs })    