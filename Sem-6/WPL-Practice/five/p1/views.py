from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SubjectForm, CarForm

# Create your views here.
def index(request):
  return HttpResponse("<h1>hello</h1>")

def student(request):
  students = []
  total_percentage = None
  if request.method == "POST":
    name = request.POST.get('name', '')
    marks = float(request.POST.get('marks', 0))
    students.append((name, marks))
  return render(request, 'p1/student.html', {
    'students': students
  })

def subject_form(request):
  ctx = {}
  form = SubjectForm(request.POST or None)
  ctx['form'] = form
  return render(request, 'p1/subject.html', ctx)

def car_form(request):
  if request.method == "POST":
    form = CarForm(request.POST)
    if form.is_valid():
      request.session['manufacturer'] = form.cleaned_data['manufacturer']
      request.session['model_name'] = form.cleaned_data['model_name']
      return redirect('car_result')
  else:
    form = CarForm()
  return render(request, 'p1/car_form.html', {'form': form})
  
def car_result(request):
  manufacturer = request.session['manufacturer']
  model_name = request.session['model_name']

  return render(request, 'p1/car_result.html', {
      'manufacturer': manufacturer,
      'model_name': model_name
  })