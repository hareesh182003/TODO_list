from django import forms
from django.forms import ModelForm
from tasks.models import Task

class Taskform(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',  # Bootstrap class for input fields
            'placeholder': 'Add new task'  # Placeholder text
        })
    )

    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'other_field_name': forms.TextInput(attrs={'class': 'form-control'}),  # Add for other fields if needed
        }
