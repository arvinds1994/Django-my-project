from django import forms
from school.models import Student

class StudentForm(forms.ModelForm):
    class Meta():
        model = Student
        fields = ('name','first_name','middle_name','surname','age','email','standerd')

        widgets = {
            'first_name':forms.TextInput(attrs={'class':'textinputclass'}),
            'middle_name':forms.TextInput(attrs={'class':'textinputclass'}),
            'surname':forms.TextInput(attrs={'class':'textinputclass'}),
            'age':forms.IntegerField(),
            'email':forms.TextInput()
        }