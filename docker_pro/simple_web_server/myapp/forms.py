from django import forms

class SimpleForm(forms.Form):
    name = forms.CharField(label="Your Name", max_length=100)
    email = forms.EmailField(label="Your Email")
