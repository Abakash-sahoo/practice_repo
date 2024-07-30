from django import forms

class StuForm(forms.Form):
    sname=forms.CharField(max_length=50,required=True)
    