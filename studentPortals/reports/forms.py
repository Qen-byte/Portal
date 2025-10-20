<<<<<<< HEAD
from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'code', 'credit_units']
=======
from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'code', 'credit_units']
>>>>>>> bbc56343274ba21683d99fc68ba04072d741c2ff
