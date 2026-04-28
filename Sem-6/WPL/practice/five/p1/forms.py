from django import forms

class SubjectForm(forms.Form):
  title = forms.CharField(max_length=100)
  desc = forms.CharField()
  views = forms.IntegerField()
  available = forms.BooleanField()

class CarForm(forms.Form):
  MANUFACTURERS = [
    ('', '-- Select Manufacturer --'),
    ('toyota', 'Toyota'),
    ('honda', 'Honda'),
    ('ford', 'Ford'),
    ('bmw', 'BMW'),
    ('audi', 'Audi'),
    ('mercedes', 'Mercedes'),
  ]
  manufacturer = forms.ChoiceField(
    choices=MANUFACTURERS,
    widget=forms.Select()
  )
  model_name = forms.CharField(max_length=100)