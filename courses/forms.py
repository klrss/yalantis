from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Назва курсу",
    "label":"Курс"}))
    begin = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control","placeholder":"Починається",
    "aria-label":"Дата початку"}))
    end = forms.DateField(widget=forms.DateInput(attrs={"class":"form-control","placeholder":"Завершується",
    "aria-label":"Дата завершення"}))
    number = forms.IntegerField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Кількість лекцій",
    "aria-label":"Кількість лекцій"}),required=True)

    class Meta():
        model = Course
        fields = ("__all__")
